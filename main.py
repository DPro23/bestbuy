from products import Product
from store import Store


# setup initial stock of inventory
product_list = [ Product("MacBook Air M2", price=1450, quantity=100),
                 Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


def start(store: Store):
    while True:
        cli = input('''
            --- Store Menu ---
            1. List all products in store
            2. Show total amount in store
            3. Make an order
            4. Quit
            Please choose a number: ''')

        if cli == '1':
            print_all_products(store)
        if cli == '2':
            print(f"Total of {store.get_total_quantity()} items in the store")
        if cli == '3':
            print_all_products(store)
            product_to_order = input('''When you want to finish order, enter empty text.
                Which product # do you want? ''')
            if product_to_order == '':
                continue
            order_amount = int(input('What amount do you want? '))
            store.order([(store.get_all_products()[int(product_to_order) - 1], order_amount)])
            print('Product added to list!')
        if cli == '4':
            break


def print_all_products(store: Store):
    print('-' * 5)
    for idx, product in enumerate(store.get_all_products()):
        print(f'{idx + 1}. {product.name}, Price: {product.price}, Quantity: {product.quantity}')
    print('-' * 5)


start(best_buy)