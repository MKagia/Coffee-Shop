import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def test_coffee_name_valid():
    coffee = Coffee("Latte")
    assert coffee.name == "Latte"

def test_coffee_name_too_short():
    with pytest.raises(ValueError):
        Coffee("No")

def test_orders_and_customers():
    coffee = Coffee("Flat White")
    c1 = Customer("Sam")
    c2 = Customer("Lily")
    c1.create_order(coffee, 4.5)
    c2.create_order(coffee, 4.0)

    assert len(coffee.orders()) == 2
    assert set(coffee.customers()) == {c1, c2}

def test_num_orders():
    coffee = Coffee("Americano")
    c = Customer("Tim")
    c.create_order(coffee, 3.0)
    c.create_order(coffee, 3.5)
    assert coffee.num_orders() == 2

def test_average_price():
    coffee = Coffee("Macchiato")
    c = Customer("Zoe")
    c.create_order(coffee, 4.0)
    c.create_order(coffee, 6.0)
    assert coffee.average_price() == 5.0
