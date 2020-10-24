def subset(n,s):
    for i in range(1, 1<<n):
        a = []
        for j in range(n):
            if i & (1<<j):
                a.append(j)
        temp = a[:]
        s.append(temp)


def solution(relation):
    answer = 0
    s = []
    subset(len(relation[0]),s)
    visited = [False] * (2**len(relation) - 1)
    for r in range(len(s)):
        if visited[r]: continue
        isFail = False
        for i in range(len(relation)-1):
            if isFail: break
            for j in range(i+1,len(relation)):
                if isFail: break
                cnt = 0
                for idx in s[r]:
                    if relation[i][idx] == relation[j][idx]:
                        cnt += 1
                if cnt == len(s[r]):
                    isFail = True
                    visited[r] = True
                    break
        if not isFail:
            answer += 1
            for i in range(len(s[r])):
                if not visited[i]:
                    for y in range(len(s)):
                        if i == y: continue
                        for x in range(len(s[y])):
                            if s[y][x] == s[r][i]:
                                visited[y] = True

    return answer

ex1 = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(ex1))