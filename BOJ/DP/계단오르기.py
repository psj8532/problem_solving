N = int(input())
stairs = []
for _ in range(N):
    stairs.append(int(input()))
visited = {i:[] for i in range(N)}
if N > 1:
    visited[0].append([stairs[0], 0])
    visited[1].append([stairs[0] + stairs[1], 1])
    visited[1].append([stairs[1], 0])
    for i in range(2,len(stairs)):
        for v,c in visited[i-1]:
            if c == 0:
                visited[i].append([stairs[i]+v,1])
        temp = [0, 0]
        for v,c in visited[i-2]:
            if v > temp[0]:
                temp = [v, 0]
        temp[0] += stairs[i]
        visited[i].append(temp)
    max_val = 0
    for v,c in visited[N-1]:
        if v > max_val:
            max_val = v
    answer = max_val
else:
    answer = stairs[0]
print(answer)