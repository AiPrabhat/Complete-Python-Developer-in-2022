import random as rd

# help(random)
# print(dir(random))

# print(rd.random())
# print(rd.randint(1,100))

my_list = [1,2,3,4,5]

# print(rd.choice(my_list))
# print(rd.choices(my_list))

rd.shuffle(my_list)
print(my_list)