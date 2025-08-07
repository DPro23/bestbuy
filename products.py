class Product:
    def __init__(self, name: str, price: float, quantity: int):
        """A product with name and positive quantity is active by default"""
        try:
            if name.strip() == '' or price < 0 or quantity < 0:
                raise ValueError()
            self.name = name.strip()
            self.price = float(price)
            self.quantity = int(quantity)
            self.active = True
        except ValueError:
            print("Product error: empty name / negative price or quantity")


    def get_quantity(self) -> int:
        """Returns the product quantity (int)"""
        return self.quantity


    def set_quantity(self, quantity):
        """Sets the product quantity (int)"""
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False


    def is_active(self) -> bool:
        """Returns product active (bool)"""
        return self.active


    def activate(self):
        """Activates the product"""
        self.active = True


    def deactivate(self):
        """Deactivates the product"""
        self.active = False


    def show(self):
        """Prints a string that represents the product"""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        """
        if not self.is_active() or self.quantity < quantity:
            raise ValueError(f"There are less then {quantity} {self.name} available!")
        else:
            self.quantity -= quantity
            return self.price * quantity
