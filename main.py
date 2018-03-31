from app import game

def main():
    print(game.storyString())
    game.askIfNew()
    while game.over == False:
        game.actions()


if __name__ == '__main__':
    main()
