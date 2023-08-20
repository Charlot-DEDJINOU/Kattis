employee = {}
for _ in range(int(input())) :
    s = input().split()
    if s[1] not in employee.keys() :
        employee[s[1]] = "exit"

    res = "exited" if s[0] == "exit" else "entered" 
    anomali = "(ANOMALY)" if s[0] == employee[s[1]] else ""
    print(s[1],res,anomali)
    employee[s[1]] = s[0]