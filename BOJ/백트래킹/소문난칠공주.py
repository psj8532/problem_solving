import sys
sys.stdin = open("소문난칠공주.txt", "r")

def dfs(index,y,x):
    global flag, cnt
    if index == 6:
        flag = True
        if cnt>3: return
        t = a[:]
        t.sort()
        if t not in result:
            temp = t[:]
            result.append(temp)
        return
    for dir in range(4):
        new_y,new_x = y+direct[dir][0],x+direct[dir][1]
        if 0 <= new_y < 5 and 0 <= new_x < 5 and not visited[new_y][new_x]:
            if flag and len(a) == 7:
                ch = a.pop()
                v = visit.pop()
                r,c = v[0],v[1]
                visited[r][c] = 0
                if ch == 'Y':
                    cnt -= 1
            if stu[new_y][new_x] == 'Y':
            #     if cnt+1 > 3:
            #         continue
            #     else:
                cnt += 1
            visited[new_y][new_x] = 1
            visit.append((new_y,new_x))
            a.append(stu_num[new_y][new_x])
            dfs(index+1,new_y,new_x)

    if flag:
        ch = a.pop()
        v = visit.pop()
        r, c = v[0], v[1]
        visited[r][c] = 0
        if ch == 'Y':
            cnt -= 1


direct = [(-1,0),(0,1),(1,0),(0,-1)]
stu = [list(input()) for _ in range(5)]
result = []
stu_num = [[0]*5 for _ in range(5)]
num = 1
for i in range(5):
    for j in range(5):
        stu_num[i][j] = num
        num += 1
for i in range(5):
    for j in range(5):
        if stu[i][j] == 'S':
            a = [stu_num[i][j]]
            cnt = 0
            visited = [[0]*5 for _ in range(5)]
            visited[i][j] = 1
            visit = [(i,j)]
            flag = False
            dfs(0,i,j)
print(len(result))
for row in result:
    print(*row)
