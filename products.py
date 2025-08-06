class Product:
    def __init__(self, name: str, price: float, quantity: int):
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
        return self.quantity


    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity <= 0:
            self.active = False


    def is_active(self) -> bool:
        return self.active


    def activate(self):
        self.active = True


    def deactivate(self):
        self.active = False


    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")


    def buy(self, quantity: int) -> float:
        if not self.is_active() or self.quantity < quantity:
            raise ValueError(f"There are less then {quantity} {self.name} available!")
        else:
            self.quantity -= quantity
            return self.price * quantity


bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
mac = Product("MacBook Air M2", price=1450, quantity=100)

print(bose.buy(50))
print(mac.buy(100))
print(mac.is_active())

bose.show()
mac.show()

bose.set_quantity(1000)
bose.show()
