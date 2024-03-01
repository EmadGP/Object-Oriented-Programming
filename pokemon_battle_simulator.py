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

            challenger_naam = input("Please choose a name for the Challenger\n" )
            challenger = Trainer(challenger_naam)

    # <---------- The player gives a name to the second Trainer ---------->

            opponent_naam = input("Please choose a name for the Opponent\n")
            opponent = Trainer(opponent_naam)

            print(f"{challenger.name} VS {opponent.name}")

    # <---------- 6 Pokeball's are added to the challenger's belt ---------->

            for i in range(2):

                charmander = Charmander("Charmander")
                pokeball = Pokeball(charmander)
                challenger.takePokeball(pokeball)

                squirtle = Squirtle("Squirtle")
                pokeball = Pokeball(squirtle)
                challenger.takePokeball(pokeball)

                bulbasaur = Bulbasaur("Bulbasaur")
                pokeball = Pokeball(bulbasaur)
                challenger.takePokeball(pokeball)

        # <---------- 6 Pokeball's are added to the opponent's belt ---------->

            for i in range(2):

                charmander = Charmander("Charmander")
                pokeball = Pokeball(charmander)
                opponent.takePokeball(pokeball)

                squirtle = Squirtle("Squirtle")
                pokeball = Pokeball(squirtle)
                opponent.takePokeball(pokeball)

                bulbasaur = Bulbasaur("Bulbasaur")
                pokeball = Pokeball(bulbasaur)
                opponent.takePokeball(pokeball)

                while Rematch:

                    thrown_pokeball_c = challenger.throwPokeball()  # The challenger throws a pokeball

                    thrown_pokeball_o = opponent.throwPokeball()    # The opponent throws a pokeball

                    challenger.returnPokeball(thrown_pokeball_c)    # The challenger returns the pokeball

                    opponent.returnPokeball(thrown_pokeball_o)      # The opponent returns the pokeball

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

if __name__ == "__main__":
    main()
    