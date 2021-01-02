# 15:55 ~ 17:04
def solution(s):
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')
    ns = []
    for lst in s1:
        t = list(map(int, lst.split(',')))
        ns.append(t)
    arr = sorted(ns, key=len)
    visited = [[False] * i for i in range(1, len(arr) + 1)]

    for i in range(len(arr)):
        for num in answer:
            idx = arr[i].index(num)
            visited[i][idx] = True
        for j in range(len(arr[i])):
            if not visited[i][j]:
                answer.append(arr[i][j])
                visited[i][j] = True
                break
    return answer


#s	result
ex1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}" # [2, 1, 3, 4]
ex2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}" # [2, 1, 3, 4]
ex3 = "{{20,111},{111}}" # [111, 20]
ex4 = "{{123}}"	# [123]
ex5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}" # [3, 2, 4, 1]
print(solution(ex5))