# 16:05 ~ 16:42
# def solution(skill, skill_trees):
#     answer = 0
#     for s in skill_trees:
#         check = ''
#         for ch in s:
#             if ch in skill:
#                 check += ch
#         end = min(len(skill),len(check))
#         for i in range(end):
#             if skill[i] != check[i]:
#                 break
#         else:
#             answer += 1
#
#     return answer

# 참고한 풀이
from _collections import deque

def solution(skill, skill_trees):
    answer = 0
    for s in skill_trees:
        check = deque(skill)
        for ch in s:
            if ch in skill:
                if ch != check.popleft():
                    break
        else:
            answer += 1

    return answer

# skill	skill_trees	return
ex1 = ["CBD",["BACDE", "CBADF", "AECB", "BDA"]] # 2
print(solution(*ex1))