while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    ba, bb = 0, -1
    
    for _ in range(n):
        a, b = map(int, input().split())
        if a <= m:
            if (a * bb == b * ba and a > ba) or ba == 0 or a * bb > b * ba:
                ba = a
                bb = b
    
    if ba > 0:
        print(f"Buy {ba} tickets for ${bb}")
    else:
        print("No suitable tickets offered")