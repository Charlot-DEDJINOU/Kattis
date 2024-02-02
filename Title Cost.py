title , plafond = input().split()
plafond = float(plafond)
print(len(title) if len(title) < plafond else plafond)