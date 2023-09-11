s = input().split(';')
total = 0
for x in s :
    x = list(map(int , x.split('-')))
    total += 1 if len(x) == 1 else x[1] - x[0] + 1

print(total)