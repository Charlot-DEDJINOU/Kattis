n = int(input())
print(-1*sum([x for x in list(map(int , input().split())) if x < 0]))