class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name
        self._orders = []
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value
        def orders(self):
        return self._orders

    def coffees(self):
        unique_coffees = []
        for order in self._orders:
            if order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees

    def create_order(self, coffee, price):
        from order import Order
        order = Order(self, coffee, price)
        self._orders.append(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        
        customer_spending = {}
        for order in coffee.orders():
            customer = order.customer
            if customer not in customer_spending:
                customer_spending[customer] = 0
            customer_spending[customer] += order.price
        return max(customer_spending, key=customer_spending.get)