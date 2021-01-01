# 24분
# def solution(n):
#     ans = 0
#     here = 0
#     while True:
#         move = 1
#         ans += move
#         while here + move * 2 <= n:
#             move *= 2
#         print('현재위치: ', here)
#         here += move
#         print('이동위치: ', here, '이동해야할 위치: ', move, '건전지: ', ans)
#         if here == n:
#             break
#
#     return ans

def solution(n):
    ans = 1
    here = n
    while here != 1:
        while not here % 2:
            here //= 2
        if here != 1:
            ans += 1
            here -= 1

    return ans

ex1 = 5 #2
ex2 = 6	#2
ex3 = 5000	#5
ex4 = 1000000000
ex5 = 14
print(solution(ex3))