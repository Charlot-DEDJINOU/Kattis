game = [1,0,0]
for x in input() :
    if x == "A" :
        game[0] , game[1] = game[1] , game[0]
    elif x == "B" :
        game[1] , game[2] = game[2] , game[1]
    else :
        game[2] , game[0] = game[0] , game[2]

print(game.index(1)+1)