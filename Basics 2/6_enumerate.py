# for i,char in enumerate('Hello'):
#     print(i,char)

# for i,char in enumerate([1,2,3,4,5,6]):
#     print(i,char)

# for i,char in enumerate((1,2,3,4,5)):
#     print(i,char)

for i,char in enumerate(list(range(100))):
    print(i,char)
    if char == 50:
        print(f"index of 50 is: {i}")