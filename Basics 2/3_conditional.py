# is_old = int(input("Please enter your age: "))
# is_licensed = ''
# if (is_old < 18):
#     print('\nYou are not old enough to drive!\n')
# elif (is_old >= 18):
#     is_licensed = input("Do you have license (Yes / No): ")
#     if (is_licensed.lower() == 'no'):
#         print('\nYou are not eligible for driving, You must have driving license for driving!\n')
#     elif (is_licensed == 'yes'):
#         print("\nYou are eligible for driving!\n")
#     else:
#         print("\nSomething is wrong, Please type (Yes / No) only!\n")

# username = 'John'
# password = '123'        # Try password/username = '' and it will goto else

# if username and password:
#     print("Everything looks good!")
# else:
#     print("Something is wrong!")

# friend = True
# can_message = "Message allowed" if friend else "Not allowed to message"
# print(can_message)

# is_friend = True
# is_user = False
# if is_friend and is_user:
#     print("Bestest friends forever")

# if is_friend or is_user:
#     print("Best friends forever")

is_magician = True
is_expert = False

if is_expert and is_magician:
    print("You are a master magician")
elif is_magician and not is_expert:
    print("At least you're getting there")
elif not is_magician:
    print("You need magic powers")