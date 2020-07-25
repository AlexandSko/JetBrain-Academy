# Function "remove_p_m" removes punctuation marks
def remove_p_m(string):
    string = string.replace(" ", "")
    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.replace(":", "")
    string = string.replace(";", "")
    return string


# Function "in_put" does not allow to enter invalid values
def in_put(text):
    while True:
        try:
            inp = input(text)
            remove_p_m(inp)
            inp = inp.split()
            inp = [int(inp[i]) for i in range(len(inp))]
            # Checking number of entered coordinates (2 expected)
            if len(inp) != 2:
                print("You should enter two numbers!")
            else:
                # Checking whether the entered coordinates are in the valid range (from 1 to 3)
                count = 0
                for i in inp:
                    if 1 <= i <= 3:
                        count += 1
                if count == 2:
                    return inp
                else:
                    print("Coordinates should be from 1 to 3!")
        # Checking whether the entered coordinates are numbers
        except ValueError:
            print("You should enter numbers!")


# The function below prints the game field
def print_field(row):
    print("---------")
    for i in range(2, -1, -1):
        print("|", *row[i], "|", sep=" ")
    print("---------")


# Creating of empty field in the beginning of the game
rows = [list("   "), list("   "), list("   ")]

print_field(rows)

# Creating a game loop where the program asks the user to enter the cell coordinates
for move in range(9):
    if move % 2 == 0:
        symbol = 'X'
    else:
        symbol = 'O'

    # The program asks the user to enter the cell coordinates,
    # analyzes the move for correctness
    # and shows a field with the changes if everything is ok
    while True:
        c = in_put("Enter the coordinates: > ")
        if "X" in rows[c[1] - 1][c[0] - 1] or "O" in rows[c[1] - 1][c[0] - 1]:
            print("This cell is occupied! Choose another one!")
        else:
            rows[c[1] - 1][c[0] - 1] = symbol
            cols = [[rows[0][0], rows[1][0], rows[2][0]], [rows[0][1], rows[1][1], rows[2][1]],
                    [rows[0][2], rows[1][2], rows[2][2]]]
            diags = [[rows[0][0], rows[1][1], rows[2][2]], [rows[0][2], rows[1][1], rows[2][0]]]
            print_field(rows)
            break
            
    # Searching result of the game
    if ['X', 'X', 'X'] in rows or ['X', 'X', 'X'] in cols or ['X', 'X', 'X'] in diags:
        print("X wins")
        break
    elif ['O', 'O', 'O'] in rows or ['O', 'O', 'O'] in cols or ['O', 'O', 'O'] in diags:
        print("O wins")
        break
else:
    print("Draw")
