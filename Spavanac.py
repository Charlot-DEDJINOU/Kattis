h , min = map(int , input().split())
heure = 60*h + min - 45
h = heure//60 if heure//60 >=0 else 23
print(h , heure%60)