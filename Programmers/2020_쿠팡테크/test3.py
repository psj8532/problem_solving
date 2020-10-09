def solution(k,score):
    answer = len(score)
    diff = dict()
    count = dict()
    for i in range(1,len(score)):
        val = score[i-1] - score[i]
        if val in diff:
            diff[val].add(i-1)
            diff[val].add(i)
            count[val] += 1
        else:
            diff[val] = set()
            diff[val].add(i-1)
            diff[val].add(i)
            count[val] = 1
    result = set()
    for key in diff:
        if count[key] >= k:
            result = result|diff[key]
    answer -= len(result)
    return answer


ex1 = 3,[24,22,20,10,5,3,2,1]
ex2 = 2,[1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]
print(solution(*ex1))