dominant = { 'A' : 11, 'K' : 4 , 'Q' : 3, 'J' : 20, 'T' : 10, '9' : 14, '8' : 0, '7' : 0 }
no_dominant = { 'A' : 11, 'K' : 4 , 'Q' : 3, 'J' : 2, 'T' : 10, '9' : 0, '8' : 0, '7' : 0 }

s = input().split()
total = 0
for i in range(int(s[0]) * 4) :
    n = input()
    if n[1] == s[1] :
        total += dominant[n[0]]
    else :
        total += no_dominant[n[0]]

print(total)