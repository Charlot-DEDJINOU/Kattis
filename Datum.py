start_father = 170
mois = [31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31]
fin_mois = 0

def bixetille(annee) :
    return int(annee % 4 == 0 and annee  % 100 != 0 ) or annee % 400 == 0

day , m = map(int , input().split())

for annee in range(2000 , 2010) :
    fin_mois = fin_mois + sum(mois[:m-1]) if annee == 2009 else fin_mois + sum(mois) + bixetille(annee)
    
fin_mois += day + bixetille(2009) if m >=2 else day
day = (fin_mois - start_father) % 7

print(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" , "Sunday"][day - 1])
