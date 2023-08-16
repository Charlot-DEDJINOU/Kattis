w = int(input())
aire = 0
for i in range(int(input())) :
    a , b = map(int , input().split())
    aire += a*b

print(aire//w)