def solution(user_id, banned_id):
    def dfs(k, lst):
        if k == C:
            sc = tuple(sorted(lst))
            v.add(sc)
            return
        for i,c in enumerate(cand[k]):
            if c in lst: continue
            dfs(k+1, lst+[c])

    def candidate():
        for i,b in enumerate(banned_id):
            bl = len(banned_id[i])
            lst = []
            for j, u in enumerate(user_id):
                if len(u) != bl: continue
                for idx in range(bl):
                    if b[idx] != u[idx] and b[idx] != '*': break
                else:
                    lst.append(u)
            temp = lst[:]
            cand.append(temp)

    v, cand = set(), []
    candidate()
    C = len(cand)
    dfs(0, [])
    return len(v)

ex1 = (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])    # 2
ex2 = (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])   # 2
ex3 = (["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]) # 3

print(solution(*ex1))
print(solution(*ex2))
print(solution(*ex3))