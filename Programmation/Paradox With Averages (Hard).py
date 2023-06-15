T = int(input())

for i in range(T):
    l = input()
    nc, ne = map(int, input().split())
    cs = list(map(int, input().split()))
    es = list(map(int, input().split()))
    somme1=sum(cs)
    somme2=sum(es)
    moy_cs = somme1/nc
    moy_es = somme2/ne
    print(len([j for j in cs if ((somme1 - j)/(nc-1) > moy_cs and (somme2 + j)/(ne+1) > moy_es)]))