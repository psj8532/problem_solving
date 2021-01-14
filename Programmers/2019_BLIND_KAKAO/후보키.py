# 16:24 ~
from itertools import combinations

def solution(relation):
    candidate = []
    for i in range(1,len(relation[0])+1):
        comb = []
        comb.extend(combinations(range(len(relation[0])),i))
        for c in comb:
            check = set()
            for num in range(len(relation)):
                lst = []
                for idx in c:
                    lst.append(relation[num][idx])
                tp = tuple(lst)
                check.add(tp)
            if len(check) == len(relation):
                candidate.append(c)
    cands = set(candidate)
    for i in range(len(candidate)-1):
        for j in range(i+1,len(candidate)):
            if len(candidate[i]) == len(set(candidate[i]).intersection(set(candidate[j]))):
                cands.discard(candidate[j])
    return len(cands)

ex1 = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
ex2 = [["100","c","aaa"],["100","c","bbb"],["400","a","sss"],["100","g","aaa"]]
ex3 =  [['a', 'aa'], ['aa', 'a'], ['a', 'a']]
print(solution(ex3))