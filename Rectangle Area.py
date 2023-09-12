x1 , y1 , x2 , y2 = map(float , input().split())

x3 , y3 = x1 , y2

h = ((x3 - x2)**2 + (y3 - y2)**2)**0.5
b = ((x3 - x1)**2 + (y3 - y1)**2)**0.5

print(h*b)