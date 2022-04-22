print('String Concatenation')
print('Hello' + ' ' + 'Andrew')
print(type(str(100)), '\n')

a = "Hello"
b = "World"
c = a + ' ' + b + '\n'
print(c)

print('Type Conversion')
    # a = str(100)
    # b = int(a)
    # c = type(b)
print(type(int(str(100))), "\n")

print('Formatted Strings')
name = 'Prabhat'
age = 22

print('First way')
print('hi ' + name + ', You are ' + str(age) + ' years old\n')

print('Second way, Using .format()')
print('hi {}, You are {} years old\n'.format('Johnny', 22))
print('hi {}, You are {} years old\n'.format(name, age))
print('hi {1}, You are {0} years old\n'.format(name, age))
print('hi {new_name}, You are {age} years old\n'.format(new_name = 'John', age = 25))

print('Using formatted string')
print(f'hi {name}, You are {age} years old\n')