# for items in [1,2,3,4,5]:
#     print(items)

# for items in [1,2,3,4,5]:
#     for x in ['a', 'b', 'c']:
#         print(items, x)

user = {
    'name': 'Prabhat',
    'age': 22,
    'can_swim': True
}

for item in user:
    print(item)
print('')

for item in user.items():
    print(item)
print('')

for item in user.keys():
    print(item)
print('')

for item in user.values():
    print(item)