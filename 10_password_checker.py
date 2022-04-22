username = input("Enter your username: ")
password = input("Enter your password: ")

password_len = len(password)
hidden_password = '*' * password_len

print(f'Hello, {username}, your password {hidden_password}, is {password_len} letters long')