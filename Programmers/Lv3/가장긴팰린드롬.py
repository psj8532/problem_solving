# def solution(s):
#     answer, N = 1, len(s)
#     for cnt in range(2, N+1):
#         for i in range(N-cnt+1):
#             mid = cnt // 2
#             left = s[i:i+mid]
#             if cnt % 2: right = s[i+mid+1:i+mid+1+mid]
#             else: right = s[i+mid:i+mid+mid]
#             right = right[::-1]
#             if left == right:
#                 answer = cnt
#                 break
#     return answer

def solution(s):
    answer, N = 1, len(s)
    for cnt in range(N, 1, -1):
        for i in range(N-cnt+1):
            mid = cnt // 2
            left = s[i:i+mid]
            if cnt % 2: right = s[i+mid+1:i+mid+1+mid]
            else: right = s[i+mid:i+mid+mid]
            right = right[::-1]
            if left == right:
                return cnt
    return answer

# s	answer
ex1 = 'abcdcba'	# 7
ex2 = 'abacde'	# 3
print(solution(ex2))