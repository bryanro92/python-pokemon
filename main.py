from app import game

def main():
    game.printIntro()
    print(game.storyString())
    game.askIfNew()
    while game.getGameOver() == False:
        game.actions()
    game.printBye()
    print("Progress saved!\nThank you for playing! See you again soon!")

if __name__ == '__main__':
    main()
