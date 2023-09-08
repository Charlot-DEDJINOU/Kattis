winner = [0,0]
for i in range(1,6) :
    s = sum(list(map(int ,  input().split())))
    winner = [i , s] if s > winner[1] else winner

print(*winner)
