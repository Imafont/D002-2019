def printcell(cells):
    print("-" * 13)
    for i in range(0, 3):
        for j in range(0, 3):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 13)


def check_col(cells):
    for i in range(0, 3):
        if cells[0][i] == cells[1][i] == cells[2][i] != ' ':
            return True
    return False

def check_row(cells):
    for i in range(0, 3):
        if cells[i][0] == cells[i][1] == cells[i][2] != ' ':
            return True
    return False

def check_diagonal(cells):
    if (cells[1][1] == cells[0][0] == cells[2][2] != ' ') or (cells[2][0] == cells[0][2] == cells[1][1] != ' '):
        return True
    return False
            

def check(cells):
    if check_col(cells) or check_row(cells) or check_diagonal(cells):
        return False
    return True


cells = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
turn = 0
printcell(cells)
while check(cells) == True:
    col = int(input("Please enter column"))
    row = int(input("Please enter row"))
    if cells[row][col] == ' ' and turn == 0:
        cells[row][col] = "X"
        turn += 1
        printcell(cells)
    elif cells[row][col] == ' ' and turn == 1:
        cells[row][col] = "O"
        turn -= 1
        printcell(cells)
    else:
        print("It is taken already, pick another place!")

if turn == 1:
    print("Player 1 wins!")
else:
    print("Player 2 wins!")
