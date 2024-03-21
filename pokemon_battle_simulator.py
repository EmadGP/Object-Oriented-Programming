from random import shuffle

from models import *
from data import *


def main():
    game_running = True
    Rematch = True

    while game_running:

        # <----------- The player start the game ----------->

        print("1. Start the game")
        print("2. Quit the game")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Game started!")

            # <---------- The player gives a name to the first Trainer ---------->

            challenger_naam = input("Please choose a name for the Challenger\n").capitalize()
            challenger = Trainer(challenger_naam)

            # <---------- The player gives a name to the second Trainer ---------->

            opponent_naam = input("Please choose a name for the Opponent\n").capitalize()
            opponent = Trainer(opponent_naam)

            print(f"{challenger.name} VS {opponent.name}")

            # <---------- The game starts with the first Trainer ---------->>

            arena = Arena(challenger, opponent)

            while Rematch:

                arena.battles += 1
                arena.fight()

                print(f"Challenger's score: {arena.challenger_score}")
                print(f"Opponent's score: {arena.opponent_score}")
                print(f"Rounds played: {arena.round}")
                print(f"Battle's: {arena.battles}")

                arena.determine_winner()

                rematch = input("Do you want to play again? (yes/no)\n")

                if rematch == "yes":
                    Rematch = True
                else:
                    Rematch = False
                    game_running = False
                    print("Game over!")
                    quit()

        # <------ The player can choose to quit the game or continue ------>

        elif choice == "2":
            print("Game over!")
            quit()
        else:
            print("Invalid choice. Please try again.")


main()
