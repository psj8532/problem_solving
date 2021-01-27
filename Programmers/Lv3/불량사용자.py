# 11:47 ~ 13:11 # 5번 케이스 시간초과 # 나중에 다시 풀기
def solution(user_id, banned_id):
    def dfs(k, ans, lst):
        if k == B:
            slst = tuple(sorted(lst))
            if slst in v:
                return ans
            # print('답: ', *lst, '/', *slst)
            v[slst] = 1
            return ans + 1
        for i in range(k, B):
            if b_visit[i]: continue # 이미 나왔으면 순서에 상관없이 포함되면 안되므로
            b, bl = banned_id[i], len(banned_id[i])
            b_visit[i] = 1
            # print(i)
            # print('금지 아이디: ', b)
            for j, u in enumerate(user_id):
                if len(u) != bl or visit[j]: continue
                for idx in range(bl):
                    if b[idx] != u[idx] and b[idx] != '*': break
                else:
                    # print('전체 아이디: ', u)
                    lst.append(u)
                    visit[j] = 1
                    ans = dfs(k+1, ans, lst)
                    visit[j] = 0
                    lst.pop()
            b_visit[i] = 0
        return ans


    answer, B, visit = 0, len(banned_id), [0] * len(user_id)
    b_visit= [0] * B
    v = {}
    answer = dfs(0, answer, [])
    return answer

ex1 = (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])    # 2
ex2 = (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])   # 2
ex3 = (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]) # 3
# print(solution(*ex1))
print(solution(*ex2))
# print(solution(*ex3))