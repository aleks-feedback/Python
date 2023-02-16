games = ["Alien Shooter", "Tic Tac Toe", "Snake", "Puzzle", "Football"]

choice = int(input())

def run(games, choise):
    if choise <= 4 and choise >= 0:
        print(games[choice])
    else:
        print("Unknown")

run(games, choice)