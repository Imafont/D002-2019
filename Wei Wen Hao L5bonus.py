def sodukucell(cells):
    print("-" * 26)
    for i in range(0, 6):
        for j in range(0, 6):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 26)

def check_number(cells):
    if (' ' not in cells[1]) and (' ' not in cells[2]) and (' ' not in cells[3]) and (' ' not in cells[4]) and (' ' not in cells[5]) and (' ' not in cells[0]):
        return False
    return True

def check_repeat(cells, number, row, col):
    for i in range(0, 6):
        if (cells[row][i] == str(number)) or (cells[i][col] == str(number)):
            return False
    return True
original = [[' ',' ','3',' ','1',' '], ['5','6',' ','3','2',' '], [' ','5','4','2',' ','3'], ['2',' ','6','4','5',' '], [' ','1','2',' ','4','5'], [' ','4',' ','1',' ',' ']]
cells = [[' ',' ','3',' ','1',' '], ['5','6',' ','3','2',' '], [' ','5','4','2',' ','3'], ['2',' ','6','4','5',' '], [' ','1','2',' ','4','5'], [' ','4',' ','1',' ',' ']]
sodukucell(cells)

while check_number(cells):
    action = input("Do you wish to remove a number or add a number? Input 'add' or 'remove'.\n")
    if action == 'add':
        col = int(input("Please enter a column:\n"))
        row = int(input("Please enter a row:\n"))
        if cells[row][col] == ' ':
            number = int(input("Please enter a number:\n"))
            if (check_repeat(cells, number, row, col)) and (number < 7) and (number > 0):
                cells[row][col] = number
                sodukucell(cells)
            else:
                print("Invalid input")
        else:
            print("That slot already has a number.")
    elif action == 'remove':
        col = int(input("Please enter a column:\n"))
        row = int(input("Please enter a row:\n"))
        change = []
        for i in range(0, 6):
            for j in range(0, 6):
                if cells[i][j] != original[i][j]:
                    change = change + [cells[i][j]]
        if cells[row][col] not in change:
            print("You can't remove that!")
        else:
            cells[row][col] = ' '
            sodukucell(cells)
    else:
        print("Invalid input.")

print("Congratsulations! You've filled the soduku board!")
