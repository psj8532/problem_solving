from itertools import combinations

def solution(info, query):
    def lower_bound(l, r, v):
        if l >= r:
            if v > scores[r]:
                return S
            return r
        mid = (l + r) // 2
        if v <= scores[mid]:
            return lower_bound(l, mid, v)
        else:
            return lower_bound(mid+1, r, v)

    answer, applicants = [], {}
    for i,data in enumerate(info):
        data = list(data.split())
        data[-1] = int(data[-1])
        score = data[-1]
        for i in range(5):
            comb = list(combinations([0, 1, 2, 3], i))
            for c in comb:
                lst = data[:4]
                for j in c:
                    lst[j] = '-'
                new_data = ''.join(lst)
                if new_data in applicants: applicants[new_data].append(score)
                else: applicants[new_data] = [score]

    for val in applicants.values():
        val.sort()

    for qry in query:
        qry = list(qry.split(' and '))
        for q in qry.pop().split():
            qry.append(q)
        qry[-1] = int(qry[-1])
        data = ''.join(qry[:4])
        if data not in applicants:
            answer.append(0)
            continue
        scores = applicants[data]
        S,score = len(scores), qry[-1]
        target = lower_bound(0, S-1, score)
        answer.append(S-target)
    return answer

ex1 = (["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"])
# [1, 1, 1, 1, 2, 4]
ex2 = (["java backend junior pizza 150"], ["- - - - 160"])
print(solution(*ex2))