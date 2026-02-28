class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def product_info(self):
        print(f"Proizvod: {self.name} whose price is: {self.price}, we have {self.quantity} of them.")
         
    def updated_value(self, value):
        if value > 0:
            self.quantity = value
            print(f"New quantity of: {self.name}: {self.quantity}")