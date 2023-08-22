for _ in range(int(input())):
    s = list(map(int, input().split()))[1:]
    moyenne = sum(s) / len(s)
    pourcentage = sum([1 for x in s if x > moyenne]) / len(s) * 100
    formatted_percentage = "{:.3f}".format(pourcentage)
    print(formatted_percentage + "%")
