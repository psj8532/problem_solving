# 13:47 ~ 15:15
# 문제 설명 부실해서 오래걸림
def solution(citations):
    citations.sort(reverse=True)
    max_val = 0
    for idx in range(len(citations)):
        h = idx+1
        rear = 0
        for i in range(len(citations)):
            if citations[i] >= h:
                rear += 1
            else:
                break
        if rear >= h and len(citations)-rear <= h:
            max_val = max(max_val, h)
    return max_val

ex1 = [3, 0, 6, 1, 5]	# 3
ex2 = [0,3,3,3,5,7]
ex3 = [0,3,3,3,5,5,7,9,10]
ex4 = [1,1,1,1,1]
ex5 = [25, 8, 5, 3, 3]
ex6 = [10, 8, 5, 4, 3]
ex7 = [13,12,11,10]
print(solution(ex1))