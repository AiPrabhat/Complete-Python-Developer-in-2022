import sys

# first = sys.argv[1]
# last = sys.argv[2]
# print(f'hiii {first} {last}')


# Exercise
from random import randint

num1, num2 = int(sys.argv[1]), int(sys.argv[2])
msg = f'\nPlease enter number between {num1}-{num2}'
answer = randint(num1, num2)

chances = 2
while True:
    try:
        print(f'\n{chances + 1} guesses left!')
        # input from user?
        guess = int(input(f'Guess a number {num1}-{num2}: '))
        # check that input is a number between num1 and num2
        if chances != 0:
            if num1 <= guess <= num2:
                # check that guess and answer is equal or not
                if guess == answer:
                    print('\nYou Win :)\nYou\'re a genius!')
                    break
                else:
                    chances -= 1
            else:
                print(msg)
        else:
            print('\nYou lose :(')
            break
    except ValueError:
        print(msg)
        continue