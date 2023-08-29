def search(end_r, end_c, start_r, start_c, group):
    queue = []
    num = Map[start_r][start_c]
    
    if groups[start_r][start_c] == 0:
        queue.append([start_r, start_c])
        
        while len(queue) > 0:
            temp_r, temp_c = queue.pop(0)
            groups[temp_r][temp_c] = group
            
            if temp_r > 0 and num == Map[temp_r-1][temp_c] and groups[temp_r-1][temp_c] == 0:
                groups[temp_r-1][temp_c] = group
                queue.append([temp_r-1, temp_c])
            if temp_c > 0 and num == Map[temp_r][temp_c-1] and groups[temp_r][temp_c-1] == 0:
                groups[temp_r][temp_c-1] = group
                queue.append([temp_r, temp_c-1])
            if temp_r < len(Map) - 1 and num == Map[temp_r+1][temp_c] and groups[temp_r+1][temp_c] == 0:
                groups[temp_r+1][temp_c] = group
                queue.append([temp_r+1, temp_c])
            if temp_c < len(Map[0]) - 1 and num == Map[temp_r][temp_c+1] and groups[temp_r][temp_c+1] == 0:
                groups[temp_r][temp_c+1] = group
                queue.append([temp_r, temp_c+1])
    
    if groups[start_r][start_c] == groups[end_r][end_c]:
        if Map[start_r][start_c] == "0":
            print("binary")
        else:
            print("decimal")
    else:
        print("neither")

Map = []
r, c = map(int, input().split())

for _ in range(r):
    Map.append(list(input()))

groups = [[0 for _ in range(c)] for _ in range(r)]

num_queries = int(input())
for i in range(num_queries):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    search(r2, c2, r1, c1, i+1)