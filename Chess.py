def black(text):  # Converts text to said colour
    return "\033[30m{}\033[0m".format(text)


def white(text):  # Converts text to said colour
    return "\033[97m{}\033[0m".format(text)


def red(text):  # Didn't use
    return "\033[31{}\033[0m".format(text)


row = 5  # Creating important variables
column = 5
piece = white(" ■")
col_start = 5
row_start = 5
turnCount = 0
turnColour = "White"
row1 = [black("R"), black("N"), black("B"), black("Q"), black("K"), black("B"), black("N"), black("R")]  # Rows in the Board
row2 = [black("1"), black("2"), black("3"), black("4"), black("5"), black("6"), black("7"), black("8")]
row3 = [white("■"), black("■"), white("■"), black("■"), white("■"), black("■"), white("■"), black("■")]
row4 = [black("■"), white("■"), black("■"), white("■"), black("■"), white("■"), black("■"), white("■")]
row5 = [white("■"), black("■"), white("■"), black("■"), white("■"), black("■"), white("■"), black("■")]
row6 = [black("■"), white("■"), black("■"), white("■"), black("■"), white("■"), black("■"), white("■")]
row7 = [white("1"), white("2"), white("3"), white("4"), white("5"), white("6"), white("7"), white("8")]
row8 = [white("R"), white("N"), white("B"), white("Q"), white("K"), white("B"), white("N"), white("R")]
boards = [row1, row2, row3, row4, row5, row6, row7, row8]  # Board is stored in this list of lists


def pawn(num, startCol, startRow, endCol, endRow):  # Checks to make sure that pawns move correctly
    if num != "1" and num != "2" and num != "3" and num != "4" and num != "5" and num != "6" and num != "7" and num != "8":
        return True
    elif abs(startCol - endCol) == 1 and abs(startRow - endRow) == 1:
        if turnColour == "Black":
            if boards[endRow - 1][endCol - 1] != black("■") and boards[endRow - 1][endCol - 1] != white(
                    "■") and endRow > startRow:
                return True
            else:
                return False
        if turnColour == "White":
            if boards[endRow - 1][endCol - 1] != black("■") and boards[endRow - 1][endCol - 1] != white("■") and endRow < startRow:
                return True
            else:
                return False
    if turnColour == "White":
        if startRow > endRow:
            return True
        elif startRow < endRow:
            return False
    if turnColour == "Black":
        if startRow < endRow:
            return True
        elif startRow > endRow:
            return False


def piece_check(piece, startCol, startRow, endCol, endRow):  # Makes sure there's no pieces in the way of the move
    if piece == "N" or piece == "K":
        return True
    elif abs(startCol - endCol) == 1 or abs(startRow - endRow) == 1:
        return True
    smallRow = min(startRow, endRow)
    bigRow = max(startRow, endRow)
    smallCol = min(startCol, endCol)
    bigCol = max(startCol, endCol)
    if smallRow == bigRow:
        bigRow += 1
    elif 1 < abs(smallRow - bigRow):
        bigRow -= 1
    if smallCol == bigCol:
        bigCol += 1
    elif 1 < abs(smallCol - bigCol):
        bigCol -= 1
    if (piece == "B") or (piece == "Q" and startCol != endCol and startRow != endRow):
        horizontalDif = abs(startCol - endCol)
        verticalDif = abs(startRow - endRow)
        for i in range(smallRow, bigRow):
            if (startCol > endCol and startRow > endRow) or (startCol < endCol and startRow < endRow):
                indexRow = smallRow + (i - smallRow)
                indexCol = smallCol + (i - smallRow)
            if startCol < endCol and startRow > endRow or startCol > endCol and startRow < endRow:
                indexRow = smallRow + (i - smallRow)
                indexCol = bigCol - (i - smallRow) - 1
            if boards[indexRow][indexCol] == black("■") or boards[indexRow][indexCol] == white("■"):
                continue
            if boards[indexRow][indexCol] != black("■") and boards[indexRow][indexCol] != white("■"):
                return False
        return True
    else:
        for i in range(smallRow - 1, bigRow - 1):
            for j in range(smallCol - 1, bigCol - 1):
                if abs(startRow - endRow) == 0:  # Horizontal Move piece-in-way check
                    if boards[i][j + 1] == black("■") or boards[i][j + 1] == white("■"):
                        continue
                    if boards[i][j + 1] != black("■") and boards[i][j + 1] != white("■"):
                        return False
                else:  # Vertical Move piece-in-way check
                    if boards[i + 1][j] == black("■") or boards[i + 1][j] == white("■"):
                        continue
                    if boards[i + 1][j] != black("■") and boards[i + 1][j] != white("■"):
                        return False
        return True


def check_move(piece_kind):  # Makes sure the piece can move like that
    if piece_kind == "R" or piece_kind == "r":  # Check if move is possible
        if col_start == column or row_start == row:
            return True
        else:
            print("Invalid Move!")
            return False
    elif piece_kind == "N" or piece_kind == "n":
        if (abs(column - col_start) == 1 and abs(row - row_start) == 2) or (
                abs(column - col_start) == 2 and abs(row - row_start) == 1):
            return True
        else:
            print("Invalid Move!")
            return False
    elif piece_kind == "B" or piece_kind == "b":
        difference = abs(col_start - column)
        if (abs(column - col_start) == difference) and (abs(row - row_start) == difference):
            return True
        else:
            print("Invalid Move!")
            return False
    elif piece_kind == "K":
        if (abs(column - col_start) == 1 and row == row_start) or (
                column == col_start and abs(row - row_start) == 1) or (
                abs(column - col_start) == 1 and abs(row - row_start) == 1):
            return True
        else:
            print("Invalid Move!")
            return False
    elif piece_kind == "Q":
        difference = abs(col_start - column)
        if (column == col_start) or (row == row_start) or (
                (abs(column - col_start) == difference) and (abs(row - row_start) == difference)):
            return True
        else:
            print("Invalid Move!")
            return False
    elif piece_kind == "1" or piece_kind == "2" or piece_kind == "3" or piece_kind == "4" or piece_kind == "5" or piece_kind == "6" or piece_kind == "7" or piece_kind == "8":
        if (column == col_start and abs(row - row_start) == 1) or (
                abs(column - col_start) == 1 and abs(row - row_start) == 1) or (
                (column == col_start and abs(row - row_start) == 2) and (row_start == 7 or row_start == 2)):
            return True
        else:
            print("Invalid Move!")
            return False
    else:
        print("Invalid Move!")
        return False


def check_pos(col, rows, piecee):  # Make sure user inputed correct starting square
    square = boards[rows - 1][col - 1]
    if turnColour == "Black":
        piecee = black(piecee)
    if turnColour == "White":
        piecee = white(piecee)
    if square == piecee:
        return True
    elif square != piecee:
        print("Incorrect starting square. Try again.")
        return False


def king_check(piece_kind, col, row):  # Check for Check
    for i in range(0, 8):
        for j in range(0, 8):
            king = boards[i][j]
            if turnColour == "White":
                if king == black("K"):
                    kingCol = j
                    kingRow = i
            if turnColour == "Black":
                if king == white("K"):
                    kingCol = j
                    kingRow = i
    kingCol = int(kingCol) + 1
    kingRow = int(kingRow) + 1
    if not piece_check(piece_kind, col, row, kingCol, kingRow):
        return False
    elif piece_kind == "R" or piece_kind == "r":
        if col == kingCol or row == kingRow:
            print("Warning! Check!")
    elif piece_kind == "N" or piece_kind == "n":
        if (abs(col - kingCol) == 1 and abs(row - kingRow) == 2) or (
                abs(col - kingCol) == 2 and abs(row - kingRow) == 1):
            print("Warning! Check!")
    elif piece_kind == "B" or piece_kind == "b":
        difference = abs(col - kingCol)
        if (abs(col - kingCol) == difference) and (abs(row - kingRow) == difference):
            print("Warning! Check!")
    elif piece_kind == "Q":
        difference = abs(col - kingCol)
        if (col == kingCol) or (row == kingRow) or (
                (abs(col - kingCol) == difference) and (abs(row - kingRow) == difference)):
            print("Warning! Check!")
    elif piece_kind == "1" or piece_kind == "2" or piece_kind == "3" or piece_kind == "4" or piece_kind == "5" or piece_kind == "6" or piece_kind == "7" or piece_kind == "8":
        if abs(col - kingCol) == 1 and abs(row - kingRow) == 1:
            print("Warning! Check!")


def ending():  # Check for end game
    king = 0
    for i in range(0, 8):
        for j in range(0, 8):
            item = boards[i][j]
            if turnColour == "Black":
                if item == white("K"):
                    king = 1
            if turnColour == "White":
                if item == black("K"):
                    king = 1
    if king == 0:
        return True
    elif king == 1:
        return False


def input_check(turn):  # Check input
    if len(turn) != 7:
        return False
    if 49 <= ord(turn[2]) <= 56 and 49 <= ord(turn[3]) <= 56 and 49 <= ord(turn[5]) <= 56 and 49 <= ord(turn[6]) <= 56:
        return True
    else:
        return False


def board():  # Create Board and update piece posistions
    print("1 2 3 4 5 6 7 8")
    print()
    if turnColour == "White":
        boards[row - 1][column - 1] = white(piece)
    if turnColour == "Black":
        boards[row - 1][column - 1] = black(piece)
    if row_start % 2 == 0:
        if col_start % 2 != 0:
            boards[row_start - 1][col_start - 1] = black("■")
        if col_start % 2 == 0:
            boards[row_start - 1][col_start - 1] = white("■")
    if row_start % 2 != 0:
        if col_start % 2 != 0:
            boards[row_start - 1][col_start - 1] = white("■")
        if col_start % 2 == 0:
            boards[row_start - 1][col_start - 1] = black("■")
    for i in range(0, 8):
        for item in boards[i]:
            print(item, end=" ")
        print("   ", i + 1)
    print()


print("--------------------------Welcome to Chess--------------------------")  # Start and explain rules
print("---------------If you don't know how to play, too bad---------------")
print("Input will be received in the form: piece, former square, new square")
print("----------------------------EG: R 81 87-----------------------------")
print("------------The column number first, then the row number------------")
board()
while True:  # Main game loop
    if turnCount % 2 == 0:
        turnColour = "White"
    elif turnCount % 2 != 0:
        turnColour = "Black"
    print(turnColour, "\'s move(R 11 18):", sep="")
    move = input()
    if input_check(move) == False:
        print("Invalid input.")
        continue
    print()
    piece = move[0]  # Split input into the piece to move from the column, row to column, row
    start = move[2:4]
    end = move[5:]
    column = int(end[0])
    row = int(end[1])
    col_start = int(start[0])
    row_start = int(start[1])
    if not check_move(piece):
        continue
    if not check_pos(col_start, row_start, piece):
        continue
    if piece_check(piece, col_start, row_start, column, row) == False:
        print("There is a piece in the way")
        continue
    if not pawn(piece, col_start, row_start, column, row):
        print("Cannot move pawn's like that!")
        continue
    turnCount += 1
    board()  # Print updated board
    if ending() == True:
        break
    king_check(piece, column, row)

print(turnColour, "won! They captured the King!")
