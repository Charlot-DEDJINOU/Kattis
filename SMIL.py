tab = input()

for i in range(len(tab)):
    if (tab[i:i+2] == ':)' or tab[i:i+2] == ';)' or tab[i:i+3] == ':-)' or tab[i:i+3] == ';-)'):
        print(i)
