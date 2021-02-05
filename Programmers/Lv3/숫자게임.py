# 19:59 ~ 20:50(대략)
def solution(A, B):
    def upper_bound(left, right, v):
        if left >= right:
            if visited[right] or v >= B[right]: return -1
            else:
                return right
        mid = (left + right) // 2
        if v < B[mid] and not visited[mid]:
            return upper_bound(left, mid, v)
        else:
            return upper_bound(mid + 1, right, v)

    answer = 0
    A.sort()
    B.sort()
    visited = [0] * len(B)
    for a in A:
        idx = upper_bound(0, len(B)-1, a)
        if idx == -1: continue
        visited[idx] = 1
        answer += 1

    return answer

# A	B	result
ex1 = ([5,1,3,7],	[2,2,6,8])	# 3
ex2 = ([2,2,2,2],	[1,1,1,1])	# 0
ex3 = ([1,10,100,500,1000],	[10,11,500,500,400])
ex4 = ([2,7,10,10,10,15,20,20],	[3,10,10,17,17,19,20,21]) # 7
print(solution(*ex1))