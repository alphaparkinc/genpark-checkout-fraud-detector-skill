"""
checkout-fraud-detector-skill: Client SDK
Evaluates geodistances, address discrepancies, and checkout ticket size risks.
"""
from __future__ import annotations
from typing import Optional


class CheckoutFraudDetectorClient:
    """
    SDK for fraud risk screening.
    """

    def audit_transaction(
        self,
        shipping_country: str,
        billing_country: str,
        ip_country: str,
        order_amount_usd: float,
    ) -> dict:
        score = 5
        reasons = []

        sc = shipping_country.upper()
        bc = billing_country.upper()
        ipc = ip_country.upper()

        if sc != bc:
            score += 35
            reasons.append("Shipping country does not match Billing country.")

        if bc != ipc:
            score += 25
            reasons.append("Billing country does not match geo-located IP address.")

        if order_amount_usd > 1000.0:
            score += 25
            reasons.append("High checkout transaction ticket size (> $1000).")

        final_score = min(100, score)
        
        if final_score >= 60:
            status = "declined"
        elif final_score >= 30:
            status = "flagged"
        else:
            status = "approved"

        return {
            "fraud_score": final_score,
            "status": status,
            "reasons": reasons,
            "requires_manual_verification": status != "approved",
        }
