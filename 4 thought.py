from itertools import product

def calculator(a , b ,signe) :
    if signe == "*" :
        return a*b
    elif signe == "/" :
        return a//b
    elif signe == "+" :
        return a+b
    
    return a-b

def display(operations , n) :
    print("4",end=" ")
    print(*operations , sep=" 4 " , end="")
    print(" 4 =",n)

def solution(n , op_permutations) :
    if not (-61 < n < 257) :
        print("no solution")
    else :
        not_found = True
        for operations in op_permutations :
            chiffres = [4, 4, 4, 4]
            operations_copy = list(operations)
            while operations_copy :
                operator = operations_copy[0]
                index = 0
                if "*" in operations_copy and "/" in operations_copy :
                    operator = "*" if operations_copy.index("*") < operations_copy.index("/") else "/"
                    index = operations_copy.index(operator) 
                elif "*" in operations_copy :
                    operator = "*"
                    index = operations_copy.index(operator)
                elif "/" in operations_copy :
                    operator = "/"
                    index = operations_copy.index(operator)

                chiffres[index] = calculator(chiffres[index] , chiffres[index + 1] , operator)
                chiffres.pop(index+1)
                operations_copy.pop(index)
        
            if chiffres[0] == n :
                display(operations , n)
                not_found = False
                break

        if not_found :
            print("no solution")


operations = ['+', '-', '*', '/']
op_permutations = list(product(operations, repeat=3))

test = int(input())

for _ in range(test) :
    solution(int(input()) , op_permutations)