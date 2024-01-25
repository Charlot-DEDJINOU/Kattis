n = input()
salles = input()
course = 0
coffee = 0
for salle in salles :
    if salle == '1' :
        coffee = 3
    
    if coffee > 0 :
        course += 1
        coffee -= 1

print(course)