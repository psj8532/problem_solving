from collections import Counter

r,c,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(3)]
R = C = 3
answer = -1
time = 0
while time <= 100:
    if r-1 < R and c-1 <C and arr[r-1][c-1] == k:
        answer = time
        break
    else:
        m_col = 0
        if R >= C: # R 연산
            for y in range(R):
                cnt = Counter(arr[y])
                if cnt.get(0): # key에 0이 있으면 제거
                    del cnt[0]
                count_num = list(map(list,cnt.items()))
                count_num.sort(key=lambda x:(x[1],x[0]))
                if len(count_num) > 50: count_num = count_num[:50]
                newArr = []
                for num,idx in count_num:
                    newArr.append(num)
                    newArr.append(idx)
                arr[y] = newArr[:]
                m_col = max(m_col,len(newArr))
            # 나머지 행의 길이를 최대 행의 길이로 맞추기
            C = m_col
            for y in range(R):
                for x in range(len(arr[y]),C):
                    arr[y].append(0)
        else:
            arr = list(map(list,zip(*arr)))
            for y in range(C):
                cnt = Counter(arr[y])
                if cnt.get(0):  # key에 0이 있으면 제거
                    del cnt[0]
                count_num = list(map(list, cnt.items()))
                count_num.sort(key=lambda x:(x[1],x[0]))
                if len(count_num) > 50: count_num = count_num[:50]
                newArr = []
                for num,idx in count_num:
                    newArr.append(num)
                    newArr.append(idx)
                arr[y] = newArr[:]
                m_col = max(m_col, len(newArr))
            # 나머지 행의 길이를 최대 행의 길이로 맞추기
            R = m_col
            for y in range(C):
                for x in range(len(arr[y]),R):
                    arr[y].append(0)
            arr = list(map(list,zip(*arr)))

    time += 1

print(answer)