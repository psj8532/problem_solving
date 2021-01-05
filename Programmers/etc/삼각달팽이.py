# 17:03 ~ 17:29
def solution(n):
    answer = []
    dy = [1,0,-1]
    dx = [0,1,-1]
    triangle = [[0]*i for i in range(1,n+1)]
    end = n*(n+1)//2
    num = dir = 0
    y,x = -1,0
    while num < end:
        ny,nx = y+dy[dir],x+dx[dir]
        if ny < 0 or ny >= n or nx < 0 or nx >= n or triangle[ny][nx] != 0:
            dir = (dir+1)%3
            ny,nx = y+dy[dir],x+dx[dir]
        num += 1
        triangle[ny][nx] = num
        y,x = ny,nx
    for row in triangle:
        answer += row
    return answer

# n	result
ex1 = 4	# [1,2,9,3,10,8,4,5,6,7]
ex2 = 5	# [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
ex3 = 6	# [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]
print(solution(ex3))