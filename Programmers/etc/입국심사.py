# 18:45 ~ 20:59
def solution(n, times):
    fail = 0
    success = max(times) * n
    while fail + 1 != success:
        cnt = 0
        mid = (fail + success) // 2
        for t in times:
            cnt += mid // t
        if cnt < n:
            fail = mid
        else:
            success = mid

    return success

# n	times	return
ex1 = [6, [7, 10]]	# 28
print(solution(*ex1))