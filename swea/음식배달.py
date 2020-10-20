def comb(index, end):
    if index == end:
        temp = a[:]
        s.append(temp)
    else:
        in_comb = [False] * len(rest)
        for i in range(index):
            in_comb[a[i]] = True
        for i in range(len(rest)-1, -1, -1):
            if in_comb[i]:
                posi = i + 1
                break
        else:
            posi = 0
        c = [0] * len(rest)
        cnt = 0
        for i in range(posi, len(rest)):
            if not in_comb[i]:
                c[cnt] = i
                cnt += 1
        for i in range(cnt):
            a[index] = c[i]
            comb(index+1, end)



direct = [(-1,0), (0,1), (1,0), (0,-1)]
t = int(input())
for tc in range(1,t+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    rest = []
    house = []
    answer = 9876543210
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > 1:
                rest.append([i,j])
            elif matrix[i][j] == 1:
                house.append([i,j])
    s = []
    for i in range(1,len(rest)+1):
        a = [0] * i
        comb(0,i)
    
    for r in range(len(s)):
        total = 0
        for hy,hx in house:
            distance = []
            for c in range(len(s[r])):
                idx = s[r][c]
                y,x = rest[idx][0],rest[idx][1]
                distance.append(abs(hy-y) + abs(hx-x))
            total += min(distance)
        for c in range(len(s[r])):
            idx = s[r][c]
            y,x = rest[idx][0],rest[idx][1]
            total += matrix[y][x]
        if total < answer:
            answer = total
    print('#{} {}'.format(tc,answer))