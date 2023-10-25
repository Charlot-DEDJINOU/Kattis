def transposition(matrix) :
    transpose = [[0]* len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)) :
        for j in range(len(matrix)) :
            transpose[j][i] = matrix[i][j]

    return transpose

def verify(matrix) :
    for s in matrix :
        if s.count('W') != s.count('B') :
            return 0
        else :
            tmp = "".join(s)
            if tmp.count("WWW") > 0 or tmp.count("BBB") > 0 :
                return 0
    
    return 1


n = int(input())
board = []

for _ in range(n) :
    s = [x for x in input()]
    board.append(s)

if verify(board) and verify(transposition(board)) :
    print(1)
else :
    print(0)