s = input()
number = input()
for i in range(0,len(number),3) :
    index = int(number[i:i+3])
    print(s[index-1] , end="")