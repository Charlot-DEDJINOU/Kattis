limit , event = map(int , input().split())
refus , number = 0 , 0
for _ in range(event) :
    s = input().split()
    if s[0] == "enter" :
        if number + int(s[1]) <= limit :
            number += int(s[1])
        else :
            refus +=1
    else :
        number -= int(s[1])

print(refus)