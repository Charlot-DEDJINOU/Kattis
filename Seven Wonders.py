t = 0
c = 0
g = 0

tab = input()

for char in tab:
    if char == 'C':
        c += 1
    elif char == 'G':
        g += 1
    else:
        t += 1

n = min(c, g, t)
result = t*t + c*c + g*g + n*7
print(result)
