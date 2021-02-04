# # 효율성 6개 맞음 => 7 => 다 맞음
def solution(gems):
    def check(s, e, l):
        if not answer: return True
        elif l < min_v:
            return True
        return False

    answer, G, min_v = [], len(set(gems)), 0
    gem_idx, cand = {}, set()
    start = 1
    for i, gem in enumerate(gems):
        cur = i + 1
        if gem in gem_idx and gem_idx[gem] == start:
            ts = cur
            for g in gem_idx:
                if gem != g and gem_idx[g] < ts:
                    ts = gem_idx[g]
            start = ts
        gem_idx[gem] = cur
        cand.add(gem)
        if len(cand) != G: continue
        if check(start, cur, cur - start + 1):
            min_v = cur - start + 1
            answer = [start, cur]
    return answer

ex1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] # [3, 7]
ex2 = ["AA", "AB", "AC", "AA", "AC"]    # [1, 3]
ex3 = ["XYZ", "XYZ", "XYZ"] # [1, 1]
ex4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"] # [1,5]
print(solution(ex1))
