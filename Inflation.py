ballon = [i for i in range(1 , int(input()) + 1)]
hellium = sorted(list(map(int , input().split())))
mini , possible = hellium[0] / ballon[0] , True

for i in range(len(ballon)) :
    if hellium[i] > ballon[i] :
        possible = False
        break
    else :
        mini = min(mini , hellium[i] / ballon[i])

if possible :
    print(mini)
else :
    print("impossible")