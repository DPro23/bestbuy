from products import Product


class Store:
    """Contains methods to manage a list of products"""
    def __init__(self, products: list[Product]):
        """Store handles a list of products"""
        self.products = products


    def add_product(self, product):
        """Add a product to the store"""
        self.products.append(product)


    def remove_product(self, product):
        """Removes a product from store"""
        self.products.remove(product)


    def get_total_quantity(self) -> int:
        """Returns how many items are in the store in total"""
        total_quantity = 0
        for product in self.products:
            total_quantity += product.quantity
        return total_quantity


    def get_all_products(self) -> list[Product]:
        """Returns all products in the store that are active"""
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products


    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order
        """
        total_price = 0.0
        for order_product in shopping_list:
            if order_product[0] in self.products:
                product, quantity = order_product
                product_quantity = order_product[0].get_quantity()
                if quantity > product_quantity:
                    print(f'There are only {product_quantity} available in the store!')
                    raise ValueError()
                product_price = product.buy(quantity)
                total_price += product_price

        return total_price
