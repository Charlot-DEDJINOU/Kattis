def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

board = [input().split() for _ in range(3)]

if check_winner(board, 'X'):
    print("Johan har vunnit")
elif check_winner(board, 'O'):
    print("Abdullah har vunnit")
else:
    print("ingen har vunnit")
