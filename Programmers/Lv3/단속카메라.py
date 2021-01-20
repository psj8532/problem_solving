# 11:35 ~
def solution(routes):
    answer = 0
    visited = [0] * len(routes)
    routes.sort(key=lambda x:(x[1],x[0]))
    for idx,lst in enumerate(routes):
        if visited[idx]: continue
        s, e = lst
        for i in range(idx+1,len(routes)):
            if routes[i][0] <= e <= routes[i][1]:
                visited[i] = 1
            else:
                break
        answer += 1

    return answer

# routes	return
ex1 = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]	# 2
print(solution(ex1))
