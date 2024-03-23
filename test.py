from CashRegister import CashRegister

# Define test functions using pytest
def test_initial_total():
    register = CashRegister()
    assert register.get_total() == "Total: $0.00"

def test_add_item():
    register = CashRegister()
    register.add_item("Apple", 1.99)
    assert register.get_total() == "Total: $1.99"

def test_add_multiple_items():
    register = CashRegister()
    register.add_item("Apple", 1.99, quantity=3)
    assert register.get_total() == "Total: $5.97"

def test_apply_discount():
    register = CashRegister()
    register.add_item("Apple", 1.99)
    register.add_item("Banana", 0.99)
    register.apply_discount()
    assert register.get_total() == "Total: $2.98"

def test_void_last_transaction():
    register = CashRegister()
    register.add_item("Apple", 1.99)
    register.add_item("Banana", 0.99)
    register.void_last_transaction()
    assert register.get_total() == "Total: $1.99"