start_father = 170
mois = sum([31 , 28 , 31 , 30 , 31 , 30 , 31 , 31 , 30 , 31 , 30 , 31])
fin_avril_annee = 0

def bixetille(annee) :
    return int(annee % 4 == 0 and annee  % 100 != 0 ) or annee % 400 == 0

n = int(input())

for annee in range(2000 , n + 1) :
    fin_avril_annee = fin_avril_annee + 120 + bixetille(annee) if annee == n else fin_avril_annee + mois + bixetille(annee)
    
jour_fin_avril = (fin_avril_annee - start_father) % 7

mother_day = 7 - jour_fin_avril + 7 + fin_avril_annee

fin_mai_annee = fin_avril_annee + 31
jour_fin_mai = (fin_mai_annee - start_father) % 7
father_day = 7 - jour_fin_mai + 14 + fin_mai_annee

print((father_day - mother_day)//7,"weeks")