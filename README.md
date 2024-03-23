# Cash-Register-Lab
# Cash Register

This Python class, `CashRegister`, is designed to simulate the functionality of a cash register. It allows you to add items with prices and quantities, apply discounts, void the last transaction, and retrieve the total.

## Usage

### Initialization
```python
from CashRegister import CashRegister

# Create a CashRegister object with an optional discount rate
register = CashRegister(discount=10)  # 10% discount
