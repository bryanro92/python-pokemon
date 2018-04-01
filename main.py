from app import game

def main():
    print(game.storyString())
    game.askIfNew()
    while game.getGameOver() == False:
        game.actions()
    print("Thank you for playing! See you again soon!")

if __name__ == '__main__':
    main()
