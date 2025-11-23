from customer import Customer
from coffee import Coffee
from order import Order

def debug_coffee_shop():
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    charlie = Customer("Charlie")
    
    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    cappuccino = Coffee("Cappuccino")
     # Create orders
    order1 = alice.create_order(latte, 4.5)
    order2 = alice.create_order(espresso, 3.0)
    order3 = bob.create_order(latte, 4.5)
    order4 = bob.create_order(cappuccino, 5.0)
    order5 = charlie.create_order(latte, 4.5)
    order6 = charlie.create_order(latte, 4.5)
    order7 = charlie.create_order(espresso, 3.5)
    
    # Test customer methods
    print(f"Alice's orders: {len(alice.orders())}")
    print(f"Alice's coffees: {[c.name for c in alice.coffees()]}")
    