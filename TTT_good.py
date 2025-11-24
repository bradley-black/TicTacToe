import random
import itertools

winning_moves = ([0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6])

board = [" " for _ in range(9)]

for i in range(9):
    board[i] = i
    i += 1

def x_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

x_board()

for i in range(9):
    board[i] = " "


def computer_move(starter, second,nums_chosen, comp_choices):
    comp_num = random.randint(0, 8)
    while comp_num in nums_chosen:
        comp_num = random.randint(0, 8)
    if starter == "computer":
        board[comp_num] = "X"
    elif second == "computer":
        board[comp_num] = "O"
    comp_choices.append(comp_num)
    nums_chosen.append(comp_num)
    x_board()

def player1_move(starter,second, nums_chosen, user_choices):
    user_num = int(input("Please enter a number between 0 and 8: "))
    while user_num in nums_chosen or user_num >= 9 or user_num < 0:
        user_num = int(input("Please enter a number between 0 and 8: "))
    if starter == "player1":
        board[user_num] = "X"
    elif second == "player1":
        board[user_num] = "O"
    user_choices.append(user_num)
    nums_chosen.append(user_num)
    x_board()

def player2_move(starter, second, nums_chosen, user2_choices):
    user2_num = int(input("Please enter a number between 0 and 8: "))
    while user2_num in nums_chosen or user2_num >= 9 or user2_num < 0:
        user2_num = int(input("Please enter a number between 0 and 8: "))
    if starter == "player1":
        board[user2_num] = "O"
    elif second == "player1":
        board[user2_num] = "X"
    user2_choices.append(user2_num)
    nums_chosen.append(user2_num)
    x_board()

def check_win(numbers, all_number):
    for combo in itertools.combinations(numbers, 3):
        if sorted(list(combo)) in winning_moves:
            return "win"
        elif len(all_number) == 9:
            return "Tie"
    return "none"

def reset_game():
    x_board()
    for i in range(9):
        board[i] = " "
    nums_chosen = []
    user_choices = []
    user2_choices = []
    comp_choices = []
    return board, nums_chosen, user_choices, user2_choices, comp_choices

def game():
    x_board()
    nums_chosen = []
    user_choices = []
    user2_choices = []
    comp_choices = []
    option_chosen = True
    while option_chosen:
        option = int(input("\nWould you like to play the computer or another player? Type 1 for computer or 2 for player: "))
        if option == 1 or option == 2:
            option_chosen = False

    game_active = True
    if option == 1:
        choices = ["player1", "computer"]
    else:
        choices = ["player1", "player2"]
    starter = random.choice(choices)
    if starter == choices[0]:
        second = choices[1]
    else:
        second = choices[0]

    print(f"{starter} starts!")

    turns = [starter, second]
    current_index = 0

    while game_active:
        current_player = turns[current_index]

        if current_player == "player1":
            player1_move(starter,second, nums_chosen, user_choices)
            result = check_win(user_choices, nums_chosen)

        elif current_player == "player2":
            player2_move(starter, second, nums_chosen, user2_choices)
            result = check_win(user2_choices, nums_chosen)

        else: # computer
            computer_move(starter, second,nums_chosen, comp_choices)
            result = check_win(comp_choices, nums_chosen)

        if result == "win": # Check win or tie
            print(f"{current_player} wins!")
            break
        elif result == "tie":
            print("It's a tie!")
            break

        current_index = 1 - current_index

    play_again = input("\nWould you like to play again? (Y/N): ").lower()
    if play_again == "y":
        reset_game()
        game()
    else:
        print("Thank you for playing!")
        return

game()