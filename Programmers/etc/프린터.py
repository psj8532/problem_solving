def solution(priorities, location):
    answer = 0
    lst = []
    for i in range(len(priorities)):
        lst.append([priorities[i],i])
    cnt = 1
    while lst:
        here,here_idx = lst.pop(0)
        for prior,p_idx in lst:
            if here < prior:
                lst.append([here,here_idx])
                break
        else:
            if here_idx == location:
                answer = cnt
            else:
                cnt += 1
        if answer != 0:
            break

    return answer

# priorities	location	return
ex1 = [[2, 1, 3, 2], 2]	# 1
ex2 = [[1, 1, 9, 1, 1, 1], 0]	# 5
print(solution(*ex1))