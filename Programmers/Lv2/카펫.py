# 21:56 ~ 22:33
# def solution(brown, yellow):
#     answer = []
#     relation = {}
#     for b in range(yellow,0,-1):
#         q, r = yellow // b, yellow % b
#         if not r:
#             if q > b:
#                 break
#             else:
#                 relation[b] = q
#
#     for w in relation:
#         h = relation[w]
#         cnt_b = ((w + 2) * 2) + (h * 2)
#         if brown == cnt_b:
#             answer = [w+2,h+2]
#             break
#     return answer

def solution(brown, yellow):
    for d in range(1, int(yellow**(1/2))+1):
        q, r = yellow // d, yellow % d
        if not r:
            w,h = q,d
            if brown == ((w + 2) * 2) + (h * 2):
                return [w+2,h+2]

# brown	yellow	return
ex1 = (10,	2)	# [4, 3]
ex2 = (8,	1)	# [3, 3]
ex3 = (24,	24) # [8, 6]
print(solution(*ex3))