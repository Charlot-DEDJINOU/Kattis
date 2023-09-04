number_test = int(input())

for _ in range(number_test) :
    s1 = input()
    s2 = input()
    s3 = ""
    for i in range(len(s1)) :
        if(s1[i] == s2[i]) :
            s3 += "."
        else :
            s3 += "*"
    print(s1,s2,s3, sep="\n")