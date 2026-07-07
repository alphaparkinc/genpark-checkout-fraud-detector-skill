# checkout-fraud-detector-skill

> **GenPark AI Agent Skill** -- Real-time checkout fraud auditing gateway.

## Quick Start

```python
from client import CheckoutFraudDetectorClient
client = CheckoutFraudDetectorClient()
res = client.audit_transaction("US", "US", "US", 99.00)
print(res["status"])
```
