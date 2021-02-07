import sys
import time
sys.stdin = open("텀프로젝트.txt", "r")
stime = time.time()

def find_set(start, target, select):
    if start == target:
        return select + 1
    else:
        if not visited[target]:
            select = find_set(start, students[target], select + 1)
            visited[target] = 1
        else:
            return 0

T = int(input())
n = int(input())
students = [0] + list(map(int,input().split()))
visited, cycle = [0] * (n+1), [0] * (n+1)
answer = n
for i in range(1, n+1):
    if visited[i]: continue
    # answer -= find_set(i,students[i],0)
    select, start, target = 0, i, students[i]
    s = [start]
    while start != students[target]:
        if cycle[target]: break
        select += 1
        s.append(target)
        target = students[target]

print(answer)
print(time.time()-stime)