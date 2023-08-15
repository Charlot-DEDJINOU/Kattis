a , b = map(str , input().split())
a = a if a[::-1] > b[::-1] else b
print(a[::-1])