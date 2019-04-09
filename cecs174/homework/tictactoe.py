#Tic Tac Toe!

def print_board(board):
    for r in board:
        for c in r:
            if c == 0:
                print('.',end='')
            elif c == 1:
                print('X',end= '')
            else:
                print('O',end= '')
        print()


def is_valid(r, c, board):
    if board [r][c] == 0:
        return True
    return False

def is_winner(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    return False




    
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
current = 1
for i in range(9):
    print_board(board)
    if is_winner(board) == True:
        break
    r = int(input("Enter row "))
    c = int(input("Enter column "))
    while not is_valid(r,c,board):
        r = int(input("Enter row "))
        c = int(input("Enter column "))
    board[r][c] = current
    if current == 1:
        current = 2
    else:
        current = 1


