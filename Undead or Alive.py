s = input()
mort , vivant = s.count(":(") , s.count(":)")
if mort != 0 and vivant != 0 :
    print("double agent")
elif mort == 0 and vivant != 0 :
    print("alive")
elif mort != 0 and vivant == 0 :
    print("undead")
else :
    print('machine')
