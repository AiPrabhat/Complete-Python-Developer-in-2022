print(__name__)

def buy(*item):
    cart = []
    for item in item:
        item = item.capitalize()
        cart.append(item)
        print(item)

