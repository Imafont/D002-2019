cells = [[' ',' ','3',' ','1',' '], ['5','6',' ','3','2',' '], [' ','5','4','2',' ','3'], ['2',' ','6','4','5',' '], [' ','1','2',' ','4','5'], [' ','4',' ','1',' ',' ']]
def sodukucell(cells):
    print("-" * 26)
    for i in range(0, 6):
        for j in range(0, 6):
            print("| %s " % cells[i][j], end="")
        print("|")
        print("-" * 26)

sodukucell(cells)

def check_number(cells):
    for i in range(0, 6):
        if all((cells[0][i] + cells[1][i] + cells[2][i] + cells[3][i] + cells[4][i] + cells[5][i] == 21) and (cells[i][0] + cells[i][1] + cells[i][2] + cells[i][3] + cells[i][4] + cells[i][5] == 21)):
            return True
    return False

def check_repeat_col(cells):
    for i in range(0, 6):
        for j in range(0, 6):
            if cell[0][j] == cell[i][j] except cell[0]
