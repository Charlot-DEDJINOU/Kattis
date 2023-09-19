def point_in_rectangle(x1, y1, x2, y2, px, py):
    if x1 <= px <= x2 and y1 <= py <= y2:
        return True
    
    return False

def point_in_circle(x0 , y0 , r , px , py) :
    if (px - x0)**2 + (py - y0)**2 <= r**2 :
        return True
    
    return False


cibles = [input().split() for _ in range(int(input()))]
for _ in range(int(input())) :
    px, py = map(int , input().split())
    total_cibles = 0
    for cible in cibles :
        if cible[0] == "rectangle" :
            x1, y1 = int(cible[1]) , int(cible[2])
            x2, y2 = int(cible[3]) , int(cible[4])
            if point_in_rectangle(x1, y1, x2, y2, px, py) :
                total_cibles += 1
        else :
            x0 , y0 , r = int(cible[1]) , int(cible[2]) , int(cible[3])
            if point_in_circle(x0 , y0 , r , px , py) :
                total_cibles += 1
    print(total_cibles)