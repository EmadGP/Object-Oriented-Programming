from models import *
from data import *

def main():
    charmander = Charmander("Charmander")


    game_running = True

    while game_running:

    # <----------- The player start the game ----------->
        
        print("1. Start the game")
        print("2. Quit the game")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Game started!")

    # <---------- The player gives a name to the first Trainer ---------->

            challenger_naam = input("Please choose a name for the challenger\n" )
            challenger = Trainer(challenger_naam)

    # <---------- The player gives a name to the second Trainer ---------->

            opponent_naam = input("Please choose a name for the challenger\n")
            opponent = Trainer(opponent_naam)

    # <--------- The player gives a name to a charmander --------->
            
            name = str(input("Give a name to your Charmander: "))
            charmander.nickname = name

            ball = Pokeball(charmander)

            challenger.takePokeball(ball)

            for pokeball in challenger.belt:
                print(pokeball.charmander.nickname)

    # <------ The charmander does its battle cry for ten times ------>
    #
    #         for i in range(10):
    #             charmander.battle_cry()

    # <------- The player can give a new name to the same charmander -------->

            changename = int(input('would you like to change the name of your charmander?, 1. Yes 2. No  '))
            if changename == 1:
                str(input('what is the name you would like tho give: '))
            elif changename == 2:
                game_running = True

    # <------ The player can choose to quit the game or continue ------>

        elif choice == "2":
            print("Game over!")
            quit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    