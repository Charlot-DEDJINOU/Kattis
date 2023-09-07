x = 7
n = int(input())

for _ in range(n):
    tab = input()
    if tab == "Skru op!" and x < 10:
        x += 1
    if tab == "Skru ned!" and x > 0:
        x -= 1

print(x)