def nombre(a, b):
    return max(a, b) * 10 + min(a, b)

def score(a):
    high = [11, 22, 33, 44, 55, 66, 21]
    return high.index(a) if a in high else -1

def winner(a, b, c, d):
    player1_dice = nombre(a, b)
    player2_dice = nombre(c, d)
    player1_score = score(player1_dice)
    player2_score = score(player2_dice)

    if player1_score != -1 or player2_score != -1:
        if player1_score > player2_score:
            return 1
        elif player1_score == player2_score:
            return 0
        else:
            return 2

    if player1_dice > player2_dice:
        return 1
    elif player1_dice == player2_dice:
        return 0
    else:
        return 2

while True:
    a, b, c, d = map(int, input().split())
    if a == 0:
        break
    else:
        result = winner(a, b, c, d)
        if result == 0:
            print("Tie.")
        else:
            print("Player", result, "wins.")
