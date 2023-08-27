mystere , alphabet , components , win = input() , input() , 0 , ""

for letter in alphabet :
    if letter in mystere :
        mystere = [x for x in mystere if x != letter]
        if not mystere :
            win = "WIN"
            break
    else :
        components += 1
        if components == 10 :
            win = "LOSE"
            break

print(win)