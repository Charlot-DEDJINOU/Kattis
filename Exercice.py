def convert_to_base_n(number, base):
    result = ""
    while number > 0:
        remainder = number % base
        result = str(remainder) + result
        number = number // base
    return result

while True :
    n = input().split()
    if n[0] == '0' :
        break

    base , p , m = int(n[0]) , n[1] , n[2]
    p = int(p , base)
    m = int(m , base)
    reste = p % m
    print(convert_to_base_n(reste , base))