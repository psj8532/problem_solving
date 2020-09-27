def solution(flowers):
    answer = 0
    count = [0]*366
    for i in range(len(flowers)):
        for j in range(flowers[i][0],flowers[i][1]):
            count[j] = 1
    for i in range(1,366):
        if count[i]:
            answer += 1
    return answer

ex1 = [[2, 5], [3, 7], [10, 11]]
ex2 = [[3, 4],[4, 5], [6, 7], [8, 10]]
print(solution(ex2))