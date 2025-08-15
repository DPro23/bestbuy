from products import Product
from store import Store

# setup initial stock of inventory
product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = Store(product_list)


def print_all_products(store: Store):
    """Prints all products in store indexed and prettier"""
    print(f"\n{'-' * 5} PRODUCTS IN THE STORE {'-' * 5}")
    for idx, product in enumerate(store.get_all_products()):
        print(f'{idx + 1}. {product.name}, Price: ${product.price}, Quantity: {product.quantity}')
    print('-' * 30)


def start(store: Store):
    """Start a CLI asking user to choose options to manage the store"""
    while True:
        try:
            cli = input("\n🏪 STORE MENU 🏪\n"
                "1. List all products in store\n"
                "2. Show total amount in store\n"
                "3. Make an order\n"
                "4. Quit\n"
                "\n#️⃣ Please choose a number: ")

            if cli == '1':
                print_all_products(store)

            elif cli == '2':
                print(f"\n🏪 Total of {store.get_total_quantity()} items in the store")

            elif cli == '3':
                total_price = 0.0
                while True:
                    print_all_products(store)
                    product_index = input("When you want to finish order, enter empty text."
                    "\nWhich product # do you want? ")

                    if product_index == '':
                        # When order is finished, print the total_price
                        print(f"\n✅ Order completed!\n🏷️ Total order price: ${total_price}")
                        break

                    if product_index.isdigit():
                        product_index = int(product_index)

                    # Order a specific amount of a single product
                    if product_index in range(1, len(store.get_all_products()) + 1):
                        order_product = store.get_all_products()[product_index - 1]
                        order_amount = int(input('What amount do you want? '))
                        order_price = store.order([(order_product, order_amount)])
                        total_price += order_price
                        print(f"\n🏷️ Products price: ${order_price}.")
                        print(f'🛒 x{order_amount} {order_product.name} '
                              'added to your shopping list!')

            elif cli == '4':
                print('\n🏪 Leaving the store...Thank you for shopping! 🙂')
                break

            else:
                raise ValueError()

        except ValueError:
            print('\nPlease enter a valid number.')


if __name__ == '__main__':
    start(best_buy)
