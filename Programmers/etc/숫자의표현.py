# def solution(n):
#     answer = 0
#     lst = [i+1 for i in range(n)]
#     for i in range(1,n+1):
#         for j in range(n-i+1):
#             if n == sum(lst[j:j+i]):
#                 answer += 1
#     return answer

def solution(n):
    answer = 0
    lst = [i+1 for i in range(n)]
    for cnt in range(1,n):
        for i in range(cnt//2,n-cnt//2):
            if cnt % 2:
                if lst[i] * cnt > n: break
                if n == lst[i] * cnt:
                    answer += 1
            else:
                if (lst[i]+lst[i+1]) * (cnt//2) > n: break
                if n == (lst[i]+lst[i+1]) * (cnt//2):
                    answer += 1
    if n == 1:
        answer = 1
    return answer

# ex1 = 15 # 4
ex2 = 10000
print(solution(ex2))

# for i in range(1,100):
#     print(solution(i))