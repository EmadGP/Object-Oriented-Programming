<<<<<<< Updated upstream
from data import *

class Charmander:
    def __init__(self, nickname):
        self.nickname = nickname
        self.strenght = "fire"
        self.weakness = "water"

    def battle_cry(self):
        print(self.nickname + "!")
=======
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
>>>>>>> Stashed changes


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
<<<<<<< Updated upstream
            self.charmander = charmander
=======
            self.pokemon = pokemon

>>>>>>> Stashed changes
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
# in for loop ro bezar toye init, wa apped ro negah dar toye take pokeball
    def takePokeball(self):
        for i in range(6):
            charmander = Charmander("Charmander" + str(i))
            pokeball = Pokeball(charmander)

            self.belt.append(pokeball)
            if len(self.belt) > 6:
                print("You can't carry more than 6 pokeballs!")
                self.belt.remove(Pokeball)

    def throwPokeball(self, pokeball, gekeuste_charmander):
        self.belt.remove(pokeball[gekeuste_charmander])
        print("Pokeball is thrown!")
        Pokeball.open()

#for loop maken in class for toevoegen van pokeballs aan de belt

# class Throw:
#     def __init__(self, belt):
#         for pokeball in belt:
#             belt.remove[0]
#             return (pokeball)
#
#
#
# class Return:
#     def __init__(self, belt, pokeball):
#         belt.append(pokeball)
