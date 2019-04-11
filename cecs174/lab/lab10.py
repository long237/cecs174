# Tic tac toe!
def print_board(board):
    for r in board:
        for c in r:
            if c == 0:
                print(".", end="")
                print(' ',end='')
            elif c == 1:
                print("X", end="")
                print(' ',end='')
            elif c == 2:
                print("O", end="")
                print(' ',end='')
            else:
                print(c,end='')
                print(' ',end='')
        print()

def is_valid(r, c, board):
    if r < 0 or r > 2:
        return False
    if c < 0 or c > 2:
        return False
    if board[r][c] == 0:
        return True
    return False

def is_winner(board):
    #row check
    for r in range(len(board)):
        if board[r][0] == board[r][1]== board[r][2] and board[r][0] != 0:
            return True
    #column check
    for c in range(len(board)):
        if board[0][c] == board[1][c] == board[2][c] and board[0][c] !=0:
            return True
    #diagonal check
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return True
    if board[2][0] == board[1][1] == board[0][2] and board[2][0] != 0:
        return True
    return False

def print_turn(current):
    if current == 1:
        print('X\'s turn')
    else:
        print('O\'s turn')

    

def main():
    board = [['-','0','1','2'],['0',0, 0, 0], ['1',0, 0, 0], ['2',0, 0, 0]]
    current = 1
    for i in range(9):
        print_board(board)
        if is_winner(board) == True:
            break

        print_turn(current)
        r = int(input("Give Row!"))
        c = int(input("Give Column!"))
        while not is_valid(r, c, board):
            r = int(input("Give Row!"))
            c = int(input("Give Column!"))

        board[r][c] = current
        if current == 1:
            current = 2
        else:
            current = 1

main()

