# 16:13 ~ # 16:20
def solution(n,a,b):
    answer = 1
    a , b  = a - 1, b - 1
    aq, bq = a // 2, b // 2
    while aq != bq:
        aq //= 2
        bq //= 2
        answer += 1

    return answer

# N	A	B	answer
ex1 = (8, 4, 7)	# 3
print(solution(*ex1))