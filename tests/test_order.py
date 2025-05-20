import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_order_valid():
    c = Customer("Test")
    coffee = Coffee("TestCoffee")
    order = Order(c, coffee, 5.0)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 5.0

def test_order_invalid_price():
    c = Customer("Invalid")
    coffee = Coffee("InvalidCoffee")

    with pytest.raises(ValueError):
        Order(c, coffee, 0.5)

    with pytest.raises(ValueError):
        Order(c, coffee, 11.0)

def test_order_invalid_customer_type():
    coffee = Coffee("Arabica")
    with pytest.raises(TypeError):
        Order("NotCustomer", coffee, 5.0)

def test_order_invalid_coffee_type():
    c = Customer("RealCustomer")
    with pytest.raises(TypeError):
        Order(c, "NotCoffee", 5.0)
