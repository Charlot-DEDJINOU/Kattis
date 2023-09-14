n = int(input())
number = [int(input()) for _ in range(n)]
number = set(list(range(1,number[-1] + 1))) - set(number)
if len(number) : print(*sorted(number) , sep='\n')
else : print("good job")