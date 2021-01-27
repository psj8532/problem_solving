# 11:13 ~ 11:39
# 현재 좌표에서 목표 좌표로 가는 길, 목표 좌표에서 현재 좌표로 오는 길은 같은 길이라는 것에 주의
def solution(dirs):
    def exist(y,x,ny,nx):
        if (y,x) in visited:
            if (ny,nx) in visited[(y,x)]: return True
            else:
                if (ny,nx) in visited and (y,x) in visited[(ny,nx)]: return True
        else:
            if (ny, nx) in visited and (y, x) in visited[(ny, nx)]: return True
        return False

    answer = 0
    visited = {}
    D = {
        'U': [1,0],
        'D': [-1,0],
        'L': [0,-1],
        'R': [0,1],
    }
    y = x = 0
    for dir in dirs:
        ny, nx = y + D[dir][0], x + D[dir][1]
        if ny < -5 or ny > 5 or nx < -5 or nx > 5: continue
        if not exist(y,x,ny,nx) and not exist(ny,nx,y,x):
            answer += 1
            if (y,x) not in visited: visited[(y,x)] = []
            visited[(y,x)].append((ny,nx))
        y, x = ny, nx

    return answer

# dirs	answer
ex1 = 'ULURRDLLU'	# 7
ex2 = 'LULLLLLLU'	# 7
print(solution(ex1))
print(solution(ex2))