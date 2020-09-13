#11:02 ~ 11:56
def dfs(val,cnt,answer):
    if val < 10:
        answer[0] = cnt
        answer[1] = val
        return
    else:
        s = str(val)
        for i in range(len(s)-1):
            if i + 1 == len(s) - 1 and s[i + 1] == '0':
                pass
            elif s[i+1] == '0': continue
            sum = int(s[:i+1])+int(s[i+1:len(s)])
            if cnt+1 < answer[0]:
                dfs(sum,cnt+1,answer)


def solution(n):
    answer = [987654321,0]
    dfs(n,0,answer)
    return answer


ex1 = 73425
ex2 = 10007
ex3 = 9
ex4 = 1000 # ans = [3, 1]
print(solution(ex4))
