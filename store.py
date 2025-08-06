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