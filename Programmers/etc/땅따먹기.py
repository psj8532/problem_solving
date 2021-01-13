# 10:26 ~ 10:39
def solution(land):
    dp = [0] * 4
    for idx,lst in enumerate(land):
        temp = [0] * 4
        for i in range(4):
            for j,val in enumerate(lst):
                sum_val = val + dp[j]
                if i != j and sum_val > temp[i]:
                    temp[i] = sum_val
        dp = temp[:]

    return max(dp)

ex1 = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]	# 16
print(solution(ex1))