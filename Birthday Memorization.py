dates = dict()
for _ in range(int(input())) :
    name, priority, date = map(str, input().split())
    if date not in dates.keys() :
        dates[date] = [priority , name]
    else :
        tmp = dates[date]
        if int(priority) > int(tmp[0]) :
            dates[date] = [priority , name]

names = []
for value in dates.values() :
    names.append(value[1])

print(len(names))
for name in sorted(names) :
    print(name)