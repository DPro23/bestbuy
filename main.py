from products import Product
from store import Store


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
                total_order_price = 0.0
                while True:
                    print_all_products(store)
                    product_index = input("When you want to finish order, enter empty text."
                    "\n#️⃣ Which product # do you want? ")

                    # After all orders are completed, print the total order price
                    if product_index == '':
                        print(f"\n👋 Exit shopping!\n🏷️ Total spent: ${total_order_price}")
                        break

                    if product_index.isdigit():
                        product_index = int(product_index)

                    # Order a specific amount of a single product
                    if product_index in range(1, len(store.get_all_products()) + 1):
                        order_product = store.get_all_products()[product_index - 1]

                        order_amount = int(input('🛍️ What amount do you want? '))

                        # Keep cart active if amount is more then quantity
                        if order_product.quantity < order_amount:
                            print('❌ Amount must be lower than quantity!')
                            continue

                        # Finalize order and update the total order price
                        products_price = store.order([(order_product, order_amount)])
                        total_order_price += products_price

                        print(f'\n✅Order completed!'
                              f'\n🛒 x{order_amount} {order_product.name}'
                              f'\n🏷️Products price: ${products_price}\n')
                    else:
                        print(f'❌ Product #{product_index} is not in the store!')

            elif cli == '4':
                print('\n🏪 Leaving the store...Thank you for shopping! 🙂')
                break

            else:
                raise ValueError('No option selected.')

        except ValueError:
            print('\nPlease enter a valid number.')


if __name__ == '__main__':
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250)
                    ]

    # init store
    best_buy = Store(product_list)

    # start CLI
    start(best_buy)
