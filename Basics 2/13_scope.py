# Scope -> What variable do I have access to ?

a = 1


def confusion():
    a = 5
    return a


print(a)
print(confusion())

# Inside a function
# 1 -> Start with local
# 2 -> Parent local - if local is not found
# 3 -> Global -  - if local and parent local not found
# 4 -> Build in python functions.
