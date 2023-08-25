s = input()
index = s.index('(')
print("correct" if index == len(s) -index -2 else "fix")