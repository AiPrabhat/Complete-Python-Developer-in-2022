# Booleans
    # True
    # False

from traceback import print_tb


print(bool('Sting'))
print(bool(1))
print(bool(0))
print(bool())

birth_year = input("What year were you born?: ")
age = 2022 - int(birth_year)
print(f'your age is: {age}\n')

age = 2022 - float(birth_year)
print(f'your age is: {age}\n')

age = age > 18
print("If age is greater than or equals to 18 it will print True else it will print False")
print(age)

