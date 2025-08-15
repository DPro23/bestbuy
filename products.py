class Product:
    """Handles methods specifics to manage a single product."""
    def __init__(self, name: str, price: float, quantity: int):
        """A product with name and positive quantity is active by default"""
        try:
            if name.strip() == '' or price < 0 or quantity < 0:
                raise ValueError('Empty name and negative price or quantity not allowed.')
            self.name = name.strip()
            self.price = float(price)
            self.quantity = int(quantity)
            self.active = self.quantity > 0

        except ValueError:
            print("Product can't be initialized.")


    def get_quantity(self) -> int:
        """Returns the product quantity (int)"""
        return self.quantity


    def set_quantity(self, quantity):
        """Sets the product quantity (int)"""
        self.quantity = quantity
        if self.quantity <= 0:
            self.deactivate()
        else:
            self.activate()


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
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")


    def buy(self, quantity: int) -> float:
        """Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        """
        if not self.is_active() or self.get_quantity() < quantity:
            raise ValueError(f"There are less than {quantity} {self.name} available!")

        self.set_quantity(self.quantity - quantity)
        return self.price * quantity
