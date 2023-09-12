n , h , v = map(int, input().split())
geb = 0
for w in [v , n-v] :
    geb = max(geb , w*h , w*(n-h))

print(geb*4)