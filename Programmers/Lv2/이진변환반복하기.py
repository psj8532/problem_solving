# 15:29 ~ 15:43
# 1이 아니면 반복 - 이진 변환
## 1의 갯수를 세고, 그 갯수를 이진수로 바꿈

def solution(s):
    answer = [0,0]
    while s != '1':
        num = s.count('1')
        answer[1] += len(s) - num
        s = bin(num)[2:]
        answer[0] += 1
    return answer

# s	result
ex1 = "110010101001"	# [3,8]
ex2 = "01110"	# [3,3]
ex3 = "1111111"	# [4,1]
print(solution(ex3))