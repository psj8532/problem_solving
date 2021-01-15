# 19:50 ~ 20:09
def solution(people, limit):
    answer = 0
    end = len(people)
    visited = [0] * len(people)
    people.sort()
    for i in range(len(people)):
        if visited[i]: continue
        for j in range(end-1,i,-1):
            if visited[j]: continue
            elif people[i] + people[j] > limit:
                visited[j] = 1
                answer += 1
                end = j
            else:
                visited[i] = visited[j] = 1
                answer += 1
                end = j
                break
        else:
            visited[i] = 1
            answer += 1
            end = i

    return answer

ex1 = ([70, 50, 80, 50], 100)	# 3
ex2 = ([70, 80, 50], 100)	# 3
print(solution(*ex2))