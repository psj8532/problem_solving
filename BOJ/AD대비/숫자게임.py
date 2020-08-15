def comb(index):
    if index == 3:
        temp = a[:]
        s.append(temp)
    else:
        in_comb = [False] * 5
        for i in range(index):
            in_comb[a[i]] = True
        for i in range(4,-1,-1):
            if in_comb[i]:
                posi = i + 1
                break
        else:
            posi = 0
        c = [0] * 5
        cnt = 0
        for i in range(posi,5):
            if not in_comb[i]:
                c[cnt] = i
                cnt += 1
        for i in range(cnt):
            a[index] = c[i]
            comb(index+1)


def get_max(num):
    max = 0
    for i in range(len(s)):
        sum = 0
        for j in range(3):
            sum += matrix[num][s[i][j]]
            sum %= 10
        if sum > max:
            max = sum
    return max


N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
result = [0]*N
a = [0]*3
s = []
comb(0)
for idx in range(N):
    result[idx] = get_max(idx)
max_val = result[N-1]
ans = N
for i in range(N-2,-1,-1):
    if result[i] > max_val:
        max_val = result[i]
        ans = i + 1
print(ans)