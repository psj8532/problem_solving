def perm(a, k, n, leng, s):
    if leng<n:
        n=leng
    if k == n:
        temp = a[:]
        s.append(temp)
    else:
        in_perm = [False] * leng
        for i in range(k):
            in_perm[a[i]] = True
        for i in range(leng - 1, -1, -1):
            if in_perm[i]:
                posi = i + 1
                break
        else:
            posi = 0
        c = [0] * leng
        cnt = 0
        for i in range(posi, leng):
            if not in_perm[i]:
                c[cnt] = i
                cnt += 1
        for i in range(cnt):
            a[k] = c[i]
            perm(a, k + 1, n, leng, s)


def solution(road, n):
    answer = -1
    road_list = []
    for i in range(len(road)):
        if road[i] == '0':
            road_list.append(i)

    leng = len(road_list)
    s = []
    a = [0] * n
    perm(a, 0, n, leng, s)
    cnt_max = 0
    road_temp = [0] * len(road)

    for i in range(len(s)):
        for j in range(len(road)):
            road_temp[j] = road[j]
        print(*road_temp)
        for j in range(n):
            idx = road_list[s[i][j]]
            road_temp[idx] = '1'
            print(idx,end=' ')
        print()
        print(*road_temp)
        print('-----------')
        cnt = 0
        for j in range(len(road)):  # 연속된 1의 갯수 셈
            if road_temp[j] == '1':
                cnt += 1
                if cnt > cnt_max:
                    cnt_max = cnt
            else:
                cnt = 0
    answer = cnt_max
    return answer
road="001100"
n=5
result=solution(road,n)
print(result)