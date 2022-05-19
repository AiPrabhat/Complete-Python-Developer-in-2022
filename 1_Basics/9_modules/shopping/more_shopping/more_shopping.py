def say_hello(*name):
    names = []
    for name in name:
        name = 'Hello ' + name.capitalize()
        names.append(name)
        print(name)
    