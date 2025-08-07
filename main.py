from products import Product
from store import Store

# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def print_all_products(store: Store):
    """Prints all products in store indexed and prettier"""
    print(f"\n{'-' * 5} PRODUCTS IN THE STORE {'-' * 5}")
    for idx, product in enumerate(store.get_all_products()):
        print(f'{idx + 1}. {product.name}, Price: {product.price}, Quantity: {product.quantity}')
    print('-' * 30)


def start(store: Store):
    """Run the Store CLI"""
    while True:
        try:
            cli = input('''
                --- STORE MENU ---
                1. List all products in store
                2. Show total amount in store
                3. Make an order
                4. Quit
                
                Please choose a number: ''')
            if cli == '1':
                print_all_products(store)

            elif cli == '2':
                print(f"\nTotal of {store.get_total_quantity()} items in the store")

            elif cli == '3':
                while True:
                    print_all_products(store)
                    print(len(store.get_all_products()))
                    product_index = input('''When you want to finish order, enter empty text.
                    Which product # do you want? ''')
                    if product_index == '':
                        break

                    elif product_index.isdigit() and int(product_index) in range(1, len(store.get_all_products()) + 1):
                        order_product = store.get_all_products()[int(product_index) - 1]
                        order_amount = int(input('What amount do you want? '))
                        store.order([(order_product, order_amount)])
                        print('Product added to shopping list!')

            elif cli == '4':
                print('\nLeaving the store...Thank you for shopping! :)')
                break
            elif cli == '':
                continue
            else:
                raise ValueError()

        except ValueError:
            print('\nPlease enter a valid number.')


start(best_buy)
