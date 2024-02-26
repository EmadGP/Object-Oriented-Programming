import random
from data import *

class Pokemon:
    def __init__(self):
        self.nickname = random.choice(pokemon_names)
        self.strenght = "fire"
        self.weakness = "water"

    def battle_cry(self):
        for i in range(10):
            print(self.nickname + "!")


class Pokeball:
    def __init__(self, charmander):
        self.charmander = charmander
        self.contains_charmander = False

    def open(self):
        if self.charmander is not None:
            self.is_open = True
            print("Charmander is released!")
            return self.charmander.battle_cry()
        else:
            print("Pokeball is empty!")

    def close(self, charmander):
        if self.is_open:
            print("Pokeball closes!")
            self.is_open = False
            self.charmander = charmander

        else:
            print("Pokeball is already closed!")

    def HasCharmanderInside(self):

        if self.charmander:
            self.contains_charmander = True
            return True

        else:
            self.contains_charmander = False
            return False

class Trainer:

    def __init__(self, name):
        self.name = name
        self.belt = []

    def takePokeball(self, pokeball):
        try:
            if len(self.belt) >= 6:
                    raise Exception("You can't carry more than 6 pokeballs!")
            else:
                self.belt.append(pokeball)
        except Exception as error:
            print(error)

    def throwPokeball(self):

        print("Pokeball is thrown!")
        pokeball = self.belt[0]
        Pokeball.open(self.belt[0])
        self.belt.remove(self.belt[0])
        return pokeball

    def returnPokeball(self, pokeball):
        self.belt.append(pokeball)

