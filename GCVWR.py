G , T , N = map(int , input().split())
G = (G-T)*0.9
G -=sum(list(map(int ,input().split())))
print(int(G))