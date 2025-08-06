from products import Product


class Store:
    def __init__(self, product):
        self.products = product


    def add_product(self, product):
        self.products.append(product)


    def remove_product(self, product):
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        return len(self.products)


    def get_all_products(self) -> list[Product]:
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        total_price = 0
        for order_product in shopping_list:
            product, quantity = order_product
            product_price = product.buy(quantity)
            total_price += product_price
        return float(total_price)


product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250),
               ]

best_buy = Store(product_list)
products_in_store = best_buy.get_all_products()
print(best_buy.get_total_quantity())
print(best_buy.order([(products_in_store[0], 1), (products_in_store[1], 2)]))