# # 효율성 6개 맞음
def solution(gems):
    def check(s, e, l):
        if not answer: return True
        elif l < min_v:
            return True
        return False

    answer, G, min_v = [], len(set(gems)), 0
    cand = set()
    gem_idx = {}
    for i, gem in enumerate(gems):
        gem_idx[gem] = i + 1
        cand.add(gem)
        if len(cand) != G: continue
        idxs = []
        for g in gem_idx:
            idxs.append(gem_idx[g])
        start, end = min(idxs), max(idxs)
        if check(start, end, end - start + 1):
            min_v = end - start + 1
            answer = [start, end]
    return answer

ex1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"] # [3, 7]
ex2 = ["AA", "AB", "AC", "AA", "AC"]    # [1, 3]
ex3 = ["XYZ", "XYZ", "XYZ"] # [1, 1]
ex4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"] # [1,5]
print(solution(ex1))
print(solution(ex2))
print(solution(ex3))
print(solution(ex4))