import numpy as np
import random as rd

# Create and display the empty array, tictac.

tictac = np.array(["-", "-", "-", "-", "-", "-", "-", "-", "-"]).reshape(3, 3)
print(tictac, "\n\n\n\n\n\n")

# tictac asks the player if they want to play the first or second turn.
# tictac also asks the player if they want to play as X's or O's.
player_start = str(input("Would you like to go first or second? \n\n\n\n\n\n"))
print("\n\n\n\n\n\n")
player = str(input("Would you like to play X's or O's? \n\n\n\n\n\n"))

if player == "X":
    computer = "O"
elif player == "O":
    computer = "X"

print("\n\n\n")

game_on = True
move_count = 0

while game_on == True:
    player_selection = False
    while player_selection == False:
        # Computer will make the first move, if the player chooses to go second
        if player_start != "first" and move_count == 0:
            tictac[rd.randint(1, 3) - 1, rd.randint(1, 3) - 1] = computer
            move_count += 1
        # Print game board
        print("\n\n", tictac, "\n\n")
        # Ask the user for row, column input
        player_select_row = int(input("Please enter a row value (1-3): "))
        print("\n")
        player_select_column = int(input("Please enter a column value (1-3): "))
        print("\n\n")
        # Adapt input to fit the tictac board
        player_select_row -= 1
        player_select_column -= 1
        # Place a player mark on a blank space;
        # If the player chose a wrong space, the the player must input again
        # They will not lose their turn, in this case
        if tictac[player_select_row, player_select_column] == "-":
            # Assign the player's choice to a blank spot in the tictac
            tictac[player_select_row, player_select_column] = player
            player_selection = True
        else:
            input("That space is already full! Press ENTER to try again \n")


    # Win condition block
    # First, the rows and columns are scanned for a possible match (count_col_ and count_row)
    # If a possible match is detected, the for loop will scan each row item, column-by-column.
    # Each row/col element will be added to a "combination" list, and that combination will be compared to a key
    # If the key is faulty, the loop will iterate over the next column until conditions are met
    count_row_player = np.count_nonzero(tictac == player, axis = 1)
    count_col_player = np.count_nonzero(tictac == player, axis = 0)
    #print(count_row_player)
    #print(count_col_player)
    #print("\n\n")
    

    if (count_row_player == 3).any():
        cols_counted = 0
        for row in range(len(tictac[:, cols_counted])):
            rows_counted = 0
            combination = []
            for column in range(len(tictac[rows_counted, :])):
                #print(row)
                #print(column)
                #print(tictac[row, column])
                combination.append(tictac[row, column])
                rows_counted += 1
                if rows_counted == 3:
                    #print(combination)
                    if all(n == player for n in combination):
                        print("\nCongratulations! You've won! \n\n\n", tictac, "\n")
                        game_on = False
                        break
                    else:
                        cols_counted += 1


    elif (count_col_player == 3).any():
        rows_counted = 0
        for column in range(len(tictac[:, rows_counted])):
            cols_counted = 0
            combination = []
            for row in range(len(tictac[cols_counted, :])):
                #print(row)
                #print(column)
                #print(tictac[row, column])
                combination.append(tictac[row, column])
                cols_counted += 1
                if cols_counted == 3:
                    #print(combination)
                    if all(n == player for n in combination):
                        print("Congratulations! You've won! \n\n\n", tictac, "\n")
                        game_on = False
                        break
                    else:
                        rows_counted += 1


    # This is supposed to determine whether the game board is full and the game should be declared a tie 
    if (tictac == "-").any() == False:
        if game_on == True:
            print("Game over - it's a tie! \n\n\n", tictac, "\n")
            break


    # Set "computer_selection" to "False;""
    # We will set the variable to "True" after an empty space has been found
    computer_selection = False
    while computer_selection == False:
        # Assign the computer's choice to a blank spot in the tictac
        computer_select_row = rd.randint(1, 3)
        computer_select_column = rd.randint(1, 3)
        # Adapt input to fit the tictac board
        computer_select_row -= 1
        computer_select_column -= 1
        # the loop will iterate for each item in the tictac -
        # if the current item is blank ("-"), store the computer's selection there
        for rows in tictac:
            for item in rows:
                if tictac[computer_select_row, computer_select_column] == "-":
                    # Assign the computer's choice to blank spot in the tictac
                    tictac[computer_select_row, computer_select_column] = computer
                    computer_selection = True

    
    # Win condition block for the computer (made from a shell of the player win condition block)
    count_row_computer = np.count_nonzero(tictac == computer, axis = 1)
    count_col_computer = np.count_nonzero(tictac == computer, axis = 0)
    #print(count_row_computer)
    #print(count_col_computer)
    
    if (count_row_computer == 3).any():
        cols_counted = 0
        for row in range(len(tictac[:, cols_counted])):
            rows_counted = 0
            combination = []
            for column in range(len(tictac[rows_counted, :])):
                #print(row)
                #print(column)
                #print(tictac[row, column])
                combination.append(tictac[row, column])
                rows_counted += 1
                if rows_counted == 3:
                    #print(combination)
                    if all(n == computer for n in combination):
                        print("\nYou lost a game of tictac to a computer - Yikes! \n\n\n", tictac, "\n")
                        game_on = False
                        break
                    else:
                        cols_counted += 1


    elif (count_col_computer == 3).any():
        rows_counted = 0
        for column in range(len(tictac[:, rows_counted])):
            cols_counted = 0
            combination = []
            for row in range(len(tictac[cols_counted, :])):
                #print(row)
                #print(column)
                #print(tictac[row, column])
                combination.append(tictac[row, column])
                cols_counted += 1
                if cols_counted == 3:
                    #print(combination)
                    if all(n == computer for n in combination):
                        print("\nYou lost a game of tictac to a computer - Yikes! \n\n\n", tictac, "\n")
                        game_on = False
                        break
                    else:
                        rows_counted += 1

    # This is supposed to determine whether the game board is full and the game should be declared a tie 
    if (tictac == "-").any() == False:
        if game_on == True:
            print("Game over - it's a tie! \n\n\n", tictac, "\n")
            break


