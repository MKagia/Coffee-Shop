from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Alice")
c2 = Customer("Bob")
latte = Coffee("Latte")
espresso = Coffee("Espresso")

c1.create_order(latte, 5.5)
c1.create_order(espresso, 3.0)
c2.create_order(latte, 6.0)

print("Coffees Alice ordered:", [c.name for c in c1.coffees()])
print("Customers who ordered Latte:", [c.name for c in latte.customers()])
print(f"Total orders for {latte.name}: {latte.num_orders()}")
print(f"Average price of {latte.name}: {latte.average_price()}")
print("Most aficionado of Latte:", Customer.most_aficionado(latte).name)
