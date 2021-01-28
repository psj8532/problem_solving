# 9:12 ~ 11:06 # 두번재 풀이였지만 또 해설 참고했음
def solution(n):
    def promising(r,c):
        for i in range(1,r+1):
            if c-i >= 0 and col[c-i] == r-i:
                return False
            if c+i < n and col[c+i] == r-i:
                return False
        return True

    def dfs(depth, ans=0):
        if depth == n: return ans + 1
        for j in range(n):
            if col[j] != -1: continue
            if depth and not promising(depth,j): continue
            col[j] = depth
            ans = dfs(depth+1, ans)
            col[j] = -1
        return ans

    col = [-1] * n
    return dfs(0)

print(solution(12))