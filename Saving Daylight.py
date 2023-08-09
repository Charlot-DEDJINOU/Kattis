def hoursToSecond(hours) :
    return int(hours[0])*3600 + int(hours[1])*60

def secondToHours(seconds) :
    return [seconds//3600 , seconds%3600//60]

while True :
    try :
        s = input().split()
        difference = secondToHours(abs(hoursToSecond(s[-2].split(':')) - hoursToSecond(s[-1].split(':'))))
        print(s[0],s[1],s[2],difference[0],"hours",difference[1],"minutes",sep=" ")
    except:
        break