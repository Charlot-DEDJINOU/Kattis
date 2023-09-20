import re 
regex=re.compile("[0-9]+") 
x=input() 
x=regex.findall(x) 
print(int(x[0])*int(x[1])*int( x[2]))