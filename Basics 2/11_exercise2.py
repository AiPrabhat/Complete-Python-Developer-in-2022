def highest_even(li):
    evens = []
    for num in li:
        if num % 2 == 0:
            evens.append(num)
    return max(evens)

print(highest_even([10,4,5,6,7,8,2]))