# lst1 = [1, 3, 5, 7, 0.44]
# print(lst1)
# lst2 = ['Prabhat', True]
# print(lst2)
# lst3 = ['Prabhat', 1, 3, 5, 7, 0.44, True]
# print(lst3, '\n')

# amazon = ['notebooks', 'sun glasses', 'mobile phones', 'Laptops', 'Accessories', 'Toys']
# print(amazon[0])
# print(amazon[1])
# print(amazon[0:])
# print(amazon[0::2], '\n')

# amazon[0] = 'textbooks'
# print(amazon)
# print(amazon[1:4], '\n')

# new_cart = amazon
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon, '\n')

# new_cart1 = amazon[:]
# new_cart1[0] = 'index'
# print(new_cart1)
# print(amazon)

from numpy import append
from operator import index


# basket = [1,2,5,4,3, 'a', 'b', 'a']
# print(basket)

# print(len(basket))

# basket.append(100)
# print(basket)

# basket.insert(2, 100)
# print(basket)

# basket.extend([100, 101])
# print(basket)

# basket.pop()
# print(basket)

# basket.remove(3)
# print(basket)

# basket.clear()
# print(basket)

# print(basket.index('a'))
# print('x' in basket)
# print('b' in basket)
# print(basket.count('a'))



# basket = [5,2,3,1,4,9,7]
# print('\n',basket)

# basket.sort()
# print(basket)

# print(sorted(basket))
# print(basket)

# new = basket.copy()
# print(new)

# basket.sort()
# basket.reverse()
# print(basket)

# basket.sort()
# print(basket[::-1])

# print(list(range(1, 101)))
# print(list(range(101)))

# sen = ''.join(['hi ', 'my ', 'name ', 'is ', 'prabhat'])
# print(sen)

a,b,c, *other = [1,2,3,4,5,6,7,8,9]
print(other)