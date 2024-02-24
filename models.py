from data import *

class Charmander:
    def __init__(self, nickname):
        self.nickname = nickname
        self.strenght = "fire"
        self.weakness = "water"

    def battle_cry(self):
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
