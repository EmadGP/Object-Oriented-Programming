from random import shuffle
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
        super().__init__(nickname, "Water", "Grass") # weakness should be leaf but im changing it to grass

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
        self.defeated_belt = []

        # <---------- 6 Pokeball's are added to the trainers belts ---------->

        for _ in range(2):
            for pokemon, trainer in [(Charmander("Charmander"), self),
                                     (Squirtle("Squirtle"), self),
                                     (Bulbasaur("Bulbasaur"), self)]:
                pokeball = Pokeball(pokemon)
                trainer.takePokeball(pokeball)

        shuffle(self.belt)

    def takePokeball(self, pokeball):
        try:
            if len(self.belt) >= 6:
                    raise Exception("You can't carry more than 6 pokeballs!")
            else:
                self.belt.append(pokeball)
        except Exception as error:
            print(error)

    def throwPokeball(self):

        print(f"{self.name}'s Pokeball is thrown!")
        pokeball = self.belt[0]
        Pokeball.open(self.belt[0])
        self.belt.remove(self.belt[0])
        return pokeball

    def returnPokeball(self, pokeball):
        self.belt.append(pokeball)

    def defeated(self, pokeball):
        self.defeated_belt.append(pokeball)

class Arena:

    challenger_score = 0
    opponent_score = 0
    round = 0
    battles = 0

    def __init__(self, challenger, opponent):
        self.challenger = challenger
        self.opponent = opponent

    def fight(self):

        battle = Battle(self.challenger, self.opponent, self)
        outcome = battle.fight_round()
        # battle.heal_up()

    def determine_winner(self):
        if self.challenger_score > self.opponent_score:
            print(f"{self.challenger.name} wins the battle!")
        elif self.challenger_score < self.opponent_score:
            print(f"{self.opponent.name} wins the battle!")
        else:
            print("It's a tie!")

class Battle:

    def __init__(self, challenger, opponent, arena):
        self.challenger = challenger
        self.opponent = opponent
        self.challengers_pokeball = None
        self.opponents_pokeball = None
        self.winner = None
        self.arena = arena

    def fight_round(self):

        for i in range(6):
            print(f"\nRound {self.arena.round + 1}!")

            self.arena.round += 1

            if self.challengers_pokeball is None:
                self.challengers_pokeball = self.challenger.throwPokeball()
            else:
                pass

            if self.opponents_pokeball is None:
                self.opponents_pokeball = self.opponent.throwPokeball()
            else:
                pass

            if self.challengers_pokeball.pokemon.strenght == self.opponents_pokeball.pokemon.weakness:
                print(f"{self.challenger.name} wins!")
                self.opponents_pokeball.close(self.opponents_pokeball.pokemon)
                self.opponent.defeated(self.opponents_pokeball)

                self.opponents_pokeball = None
                self.winner = self.challengers_pokeball
                self.arena.challenger_score += 1

            elif self.challengers_pokeball.pokemon.weakness == self.opponents_pokeball.pokemon.strenght:
                print(f"{self.opponent.name} wins!")
                self.challengers_pokeball.close(self.challengers_pokeball.pokemon)
                self.challenger.defeated(self.challengers_pokeball)

                self.challengers_pokeball = None
                self.winner = self.opponents_pokeball
                self.arena.opponent_score += 1

            else:
                try:
                    if self.winner is None:

                        self.challenger.defeated(self.challengers_pokeball)
                        self.opponent.defeated(self.opponents_pokeball)

                        self.challengers_pokeball = None
                        self.opponents_pokeball = None
                        print("IT'S A TIE!")
                        print("Both pokemon are returned to their pokeballs!!")

                    elif self.winner == self.opponents_pokeball:
                        self.opponent.defeated(self.opponents_pokeball)
                        self.opponents_pokeball = None
                        print("It's a tie!")
                        print("Opponent's pokemon is returned to pokeball!!")

                    elif self.winner == self.challengers_pokeball:
                        self.challenger.defeated(self.challengers_pokeball)
                        self.challengers_pokeball = None
                        print("It's a tie!")
                        print("Challenger's pokemon is returned to pokeball!!")

                    else:
                        raise Exception("There went something wrong!")

                except Exception as error:
                    print(error)

        print("Game over!")

    # def heal_up(self):
    #     for pokeball in self.challenger.defeated_belt():
    #         self.challenger.returnpokeball(pokeball)
    #
    #     for pokeball in self.opponent.defeated_belt():
    #         self.opponent.returnpokeball(pokeball)