# def say_hello():
#     print('Hello')
# say_hello()

# Parameters

# def say_hello(name, emoji):
# def say_hello(name='Prabhat', emoji='😀'):      # Default Parameters
#     print(f'Hello, {name} {emoji}')

# Positional arguments
# say_hello('Prabhat', '😀')
# say_hello('Raj', '😀')
# say_hello('Vinay', '😀')

# Default arguments
# say_hello()

# Keyword arguments
# say_hello(emoji='😀', name='Prabhat')

# def sum(num1, num2):
#     return num1 + num2

# print(sum(4,5))
# print(sum(42,5))


# def sum(num1, num2):
#     def another_fun(num1, num2):
#         return num1 + num2
#     return another_fun(num1, num2)

# total = sum(10,20)
# print(total)

# def test(a):
#     '''
#     Info: This function tests and prints param a
#     '''
#     print(a)

# test('!!!!!')
# help(test)
# print(test.__doc__)



# def is_even(num):

#     if num % 2 == 0:
#         return True
#     # elif num % 2 != 0:
#     return False

# print(is_even(5))

def is_even(num):
    return num % 2 == 0

print(is_even(4))