class PlayerCharacter:

    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        if (PlayerCharacter.membership):
            self.name = name        # Attributes
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')
        
player1 = PlayerCharacter('Cindy' ,33)
player2 = PlayerCharacter('John', 23)
print(player1)
print(player1.shout())
print(player2.name)