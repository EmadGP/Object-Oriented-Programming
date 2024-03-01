import random
from abc import ABC
from data import *

class Pokemon(ABC):
    def __init__(self, nickname, strenght, weakness):
        self.nickname = nickname
        self.strenght = strenght
        self.weakness = weakness

    def battle_cry(self):
        pass

class Charmander(Pokemon):
    def __init__(self, nickname):
        super().__init__(nickname, "Fire", "Water")

    def battle_cry(self):
        print("Charmander!")

class Squirtle(Pokemon):
    def __init__(self, nickname):
        super().__init__(nickname, "Water", "Leaf")

    def battle_cry(self):
        print("Squirtle!")

class Bulbasaur(Pokemon):
    def __init__(self, nickname):
        super().__init__(nickname, "Grass", "Fire")

    def battle_cry(self):
        return print("Bulbasaur!")


class Pokeball:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.contains_pokemon = False

    def open(self):
        if self.pokemon is not None:
            self.is_open = True
            print("Pokemon is released!")
            return self.pokemon.battle_cry()
        else:
            print("Pokeball is empty!")

    def close(self, pokemon):
        if self.is_open:
            print("Pokeball closes!")
            self.is_open = False
            self.pokemon = pokemon

        else:
            print("Pokeball is already closed!")

    def HasCharmanderInside(self):

        if self.pokemon:
            self.contains_pokemon = True
            return True

        else:
            self.contains_pokemon = False
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