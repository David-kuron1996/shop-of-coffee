# debug.py

from customer import Customer
from coffee import Coffee
from orders import Order

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
    
    # Test coffee methods
    print(f"Latte orders: {latte.num_orders()}")
    print(f"Latte customers: {[c.name for c in latte.customers()]}")
    print(f"Latte average price: {latte.average_price():.2f}")
    
    # Test most_aficionado
    latte_aficionado = Customer.most_aficionado(latte)
    if latte_aficionado:
        print(f"Latte aficionado: {latte_aficionado.name}")
    else:
        print("Latte aficionado: No aficionado found")
        
    espresso_aficionado = Customer.most_aficionado(espresso)
    if espresso_aficionado:
        print(f"Espresso aficionado: {espresso_aficionado.name}")
    else:
        print("Espresso aficionado: No aficionado found")
    
    # Test invalid inputs
    try:
        invalid_customer = Customer("")  # Should raise an exception
    except ValueError as e:
        print(f"Error creating customer: {e}")
    
    try:
        invalid_coffee = Coffee("Te")  # Should raise an exception
    except ValueError as e:
        print(f"Error creating coffee: {e}")

if __name__ == "__main__":
    debug_coffee_shop()