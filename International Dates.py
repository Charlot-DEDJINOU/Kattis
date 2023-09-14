date = list(map(int , input().split('/')))
if 1 <= date[0] <= 12 and 1 <= date[1] <= 12 :
    print("either")
elif 1 <= date[0] <= 31 and 1 <= date[1] <= 12 :
    print("EU")
elif 1 <= date[0] <= 12 and 1 <= date[1] <= 31 :
    print("US")