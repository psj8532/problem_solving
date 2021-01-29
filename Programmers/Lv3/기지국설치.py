# 14:11 ~ 15:11
def solution(n, stations, w):
    answer, prev, needs = 0, 1, []
    for p in stations:
        left, right = p - w, p + w
        if left > 1:
            needs.append([prev, left])
        prev = right + 1
    if prev <= n:
        needs.append([prev, n+1])
    for start, end in needs:
        cnt, scope = end - start, 2 * w + 1
        answer += cnt // scope
        if cnt % scope:
            answer += 1
    return answer

# N	stations	W	answer
ex1 = (11,	[4, 11],	1)	# 3
ex2 = (16,	[9],	2)	# 3
print(solution(*ex1))