from multiprocessing.reduction import duplicate


picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

# for image in picture:
#     for pixel in image:
#         if (pixel):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')


# Duplicates
some_list = ['a', 'b', 'c', 'd', 'd', 'b', 'a']
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)