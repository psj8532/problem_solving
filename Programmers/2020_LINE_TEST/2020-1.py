# 10:00 ~ 10:17
def solution(boxes):
    answer = -1
    cb = [0]*100001
    box_cnt = len(boxes)
    for i in range(box_cnt):
        for j in range(2):
            cb[boxes[i][j]] += 1
    for i in range(1, 100001):
        temp = cb[i]
        temp //= 2
        if temp:
            box_cnt -= temp
    answer = box_cnt
    return answer

ex1 = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
ex2 = [[1, 2], [3, 4], [5, 6]]
ex3 = [[1, 2], [2, 3], [3, 1]]
print(solution(ex3))