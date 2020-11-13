import os

def print_menu():
    print("_" * 50)
    print(" Welcome to warehouse PyControl")
    print("_" * 50)

    print('[1] - Add Product to catalog')
    print('[2] - Display catalog')
    print('[3] - Display products out of stock')
    print('[4] - Total Stock Value')
    print('[5] - Cheapest Product')
    print('[6] - Delete Product')
    print('[7] - Update Price')
    print('[8] - Update Stock')

    print('[s] - Save Changes')
    print('[x] - Exit')

def print_header(text):
    clear()
    print('_' * 50)
    print(text)
    print('-' * 50)

def print_product_info(prod):
    print(
           str(prod.id) + "  " + 
           prod.title + "  " + 
           prod.category + "  " + 
           str(prod.stock) + "  " + 
           str(prod.price)
           )   

def clear():
    if(os.name == 'nt'):
        return os.system('cls')
    else:
        return os.system('clear')
