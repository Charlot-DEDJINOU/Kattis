s = input().lower()
day = 0

for i in range(len(s)) :
    if (i % 3 == 0 and s[i] != 'p') or (i % 3 == 1 and s[i] != 'e') or (i % 3 == 2 and s[i] != 'r'):
        day += 1

print(day)
    