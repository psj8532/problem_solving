# 16:09 ~ 16:20
def solution(nums):
    half = len(nums) // 2
    set_num = set(nums)
    l = len(set_num)
    if half < l:
        return half
    else:
        return l

# nums	result
ex1 = [3,1,2,3]	# 2
ex2 = [3,3,3,2,2,4]	# 3
ex3 = [3,3,3,2,2,2]	# 2
print(solution(ex3))