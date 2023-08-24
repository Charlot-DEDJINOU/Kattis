n = int(input())
s = [x for x in list(map(int , input().split())) if x != -1]
print(sum(s)/len(s))