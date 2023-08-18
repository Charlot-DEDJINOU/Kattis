s = input()
b = s[0]

for i in range(1,len(s)) :
    if s[i] != b[-1] :
        b += s[i]
    
print(b)