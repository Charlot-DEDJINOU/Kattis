def fibonacci(n) :
    if n < 0 :
        return " Un entier positif"
    
    a = 0
    b = 1
    
    if n == 0 : 
        return a
    elif n == 1 :
        return b
    
    for _ in range(2,n) :
        c = a + b
        b = c
        a = b

    return c

print(fibonacci(int(input())))