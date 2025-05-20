import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_customer_name_valid():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_customer_name_invalid_type():
    with pytest.raises(ValueError):
        Customer(123)

def test_customer_name_invalid_length():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_create_order():
    c = Customer("Bob")
    coffee = Coffee("Latte")
    order = c.create_order(coffee, 5.0)
    assert order.customer == c
    assert order.coffee == coffee
    assert order.price == 5.0

def test_coffees_method():
    c = Customer("Charlie")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Cappuccino")
    c.create_order(coffee1, 4.0)
    c.create_order(coffee2, 5.0)
    coffee_names = [coffee.name for coffee in c.coffees()]
    assert "Espresso" in coffee_names and "Cappuccino" in coffee_names

def test_most_aficionado():
    coffee = Coffee("Mocha")
    c1 = Customer("Daisy")
    c2 = Customer("Elon")
    c1.create_order(coffee, 3.0)
    c1.create_order(coffee, 3.0)
    c2.create_order(coffee, 4.0)
    assert Customer.most_aficionado(coffee) == c1
