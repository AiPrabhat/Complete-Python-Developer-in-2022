print(__name__)

import utility
# print(utility)

print(utility.addition(2,3))
print(utility.substract(4,1))
print(utility.multiply(4,3))
print(utility.divide(6,2.5),'\n')


import shopping.cart as sc
print(sc.buy('Coca cola', 'Layes', 'Sprite'),'\n')


from utility import divide, multiply
print(multiply(4,3))
print(divide(6,2.5),'\n')


from utility import *
print(addition(2,3))
print(substract(4,1))
print(multiply(4,3))
print(divide(6,2.5),'\n')


from shopping.more_shopping.more_shopping import *
print(say_hello('prabhat', 'sunny', 'sanjay'))

#####################################################################

# if __name__ == '__main__':

