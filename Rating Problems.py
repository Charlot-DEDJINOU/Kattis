j , v = map(int , input().split())
mini = -3*(j-v)
maxi = abs(mini)
for _ in range(v) :
    vote = int(input())
    mini += vote
    maxi += vote

print(round(mini/j,4) , round(maxi/j,4))