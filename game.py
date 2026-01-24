import random as r

class InvalidInputException(Exception):
    pass

def cardinal_board():
    row_one = [[1],[2],[3]]
    row_two = [[4],[5],[6]]
    row_three = [[7],[8],[9]]
    print(row_one)
    print(row_two)
    print(row_three)
    print("\n")
    
row_one = [" "," "," "]
row_two = [" "," "," "]
row_three = [" "," "," "]

def progress_board(place, symbol):
    if place < 4:
        row_one[place - 1] = symbol
    elif place < 7:
        row_two[place - 4] = symbol
    else:
        row_three[place - 7] = symbol
    print(row_one)
    print(row_two)
    print(row_three)
    print("\n")


print("Welcome to Tic-Tac-Toe game!\n What kind of game do you want to play?")

while True:
    try:
        game_type = input("Type \"a\" for a single player game\nType \"b\" for 2 players game\n").strip().lower()
        if game_type not in ("a", "b"):
            raise InvalidInputException
        break
    except InvalidInputException:
        print("Invalid Input")


player_one = input("Enter Player-1 name: ")
if game_type == "b":
    while True:
        try:
            player_two = input("Enter Player-2 name: ")
            if player_two == player_one:
                raise InvalidInputException
            break
        except InvalidInputException:
            print("Player's names cannot be same. \nPlease enter a different name for Player-2")

print("Let us start the game\nWho wants to go first? Let us decide by Toss!\n{player_one} calls the toss".format(player_one = player_one))

while True:
    try:
        choice = input("Heads or Tails? Enter \"H\" for heads or \"T\" for Tails\n").strip().upper()
        if choice not in ("H","T"):
            raise InvalidInputException
        break
    except InvalidInputException:
        print("Invalid Input")

toss = r.choice(["H","T"])
if toss == 'H':
    toss_result = "Heads"
else:
    toss_result = "Tails"

print("Toss turned out to be {toss_result}".format(toss_result = toss_result))
if game_type == 'b':
    if choice == toss.strip().upper():
        print("{player_one} won the toss! They will have the first move".format(player_one = player_one))
        toss_winner = player_one
        toss_loser = player_two
    else:
        print("{player_two} won the toss! They will have the first move".format(player_two = player_two))
        toss_winner = player_two
        toss_loser = player_one
else:
    if choice == toss.strip().upper():
        print("{player_one} won the toss! They will have the first move".format(player_one = player_one))
        toss_winner = player_one
        toss_loser = "Computer"
    else:
        print("Computer won the toss! It will have the first move")
        toss_winner = "Computer"
        toss_loser = player_one

print("Since {toss_winner} has won the toss, {toss_loser} will choose either \"X\" or \"O\" symbol to play with".format(toss_winner = toss_winner, toss_loser = toss_loser))
while True:
    try:
        second_symbol = input("{toss_loser}, please choose the symbol!\n".format(toss_loser = toss_loser)).strip().upper()
        if second_symbol == "X":
            first_symbol = "O"
            print("{toss_loser} chooses \"X\". {toss_winner} will start with  \"O\"!".format(toss_loser = toss_loser, toss_winner = toss_winner))
        elif second_symbol == "O":
            first_symbol = "X"
            print("{toss_loser} chooses \"O\". {toss_winner} will start with  \"X\"!".format(toss_loser = toss_loser, toss_winner = toss_winner))
        else:
            raise InvalidInputException
        break
    except InvalidInputException:
        print("Invalid Input")

print("Let us finally start the game!\n {toss_winner}, please play the first move by entering the co-ordinate where you want to place {first_symbol}".format(toss_winner = toss_winner, first_symbol = first_symbol))

place_tracker = {
        "X" : [],
        "O" : []
        }
winning_combinations = [(1,2,3), (4,5,6), (7,8,9), (1,4,7), (2,5,8), (3,6,9), (1,5,9), (3,5,7)]
for i in range(0,9):
    if i % 2 == 0:
        cardinal_board()
        while True:
            try:
                place = input("{toss_winner}'s turn:\n".format(toss_winner = toss_winner))
                if int(place) in place_tracker.values():
                    raise InvalidInputException
                break
            except InvalidInputException:
                print("Place already occupied by one of the symbols. Enter unoccupied co-ordinate")
        progress_board(int(place), first_symbol)
        place_tracker[first_symbol].append(int(place))
        if i >= 4 and any(all(x in place_tracker[first_symbol] for x in t) for t in winning_combinations):
            result = toss_winner
            print("{first_symbol} is aligned for a winning combination. {toss_winner} wins the game!".format(first_symbol = first_symbol, toss_winner = toss_winner))
            break
    else:
        cardinal_board()
        while True:
            try:
                place = input("{toss_loser}'s turn:\n".format(toss_loser = toss_loser))
                if int(place) in place_tracker.values():
                    raise InvalidInputException
                break
            except InvalidInputException:
                print("Place already occupied by one of the symbols. Enter unoccupied co-ordinate")
        progress_board(int(place), second_symbol)
        place_tracker[second_symbol].append(int(place))
        if i >= 4 and any(all(x in place_tracker[second_symbol] for x in t) for t in winning_combinations):
            result = toss_loser
            print("{second_symbol} is aligned for a winning combination. {toss_loser} wins the game!".format(second_symbol = second_symbol, toss_loser = toss_loser))
            break



