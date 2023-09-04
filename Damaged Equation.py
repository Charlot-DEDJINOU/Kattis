def calculator(a, b, signe):
    if signe == "*":
        return a * b
    elif signe == "/":
        if b == 0:
            return None 
        return a // b
    elif signe == "+":
        return a + b
    elif signe == "-":
        return a - b
    else:
        return None

operations = ['*', '+', '-', '/']

a, b, c, d = map(int, input().split())
found = False

for sign1 in operations:
    for sign2 in operations:
        result1 = calculator(a, b, sign1)
        result2 = calculator(c, d, sign2)
        if result1 is not None and result2 is not None and result1 == result2:
            found = True
            print(a, sign1, b, "=", c, sign2, d)

if not found:
    print("problems ahead")