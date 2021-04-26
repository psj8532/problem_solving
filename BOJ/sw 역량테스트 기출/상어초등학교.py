direct = [(-1,0), (0,1), (1,0), (0,-1)]
Y, X, DIRECTION = 0, 1, 4
N = int(input())
student_info = {}
total_student = N ** 2
for _ in range(total_student):
    information = list(map(int,input().split()))
    student_info[information[0]] = information[1:]

placement = [[0]*N for _ in range(N)]
visit = {(i,j): True for i in range(N) for j in range(N)}
for student, info in student_info.items():
    cand = []
    for y, x in visit.keys():
        like, blank = 0, 0
        for dir in range(DIRECTION):
            ny, nx = y + direct[dir][Y], x + direct[dir][X]
            if 0 <= ny < N and 0 <= nx < N:
                if placement[ny][nx] and placement[ny][nx] in info: like += 1
                elif not placement[ny][nx]: blank += 1
        cand.append([-like, -blank, y, x])
    cand = sorted(cand)
    like, blank, y, x = cand[0]
    placement[y][x] = student
    visit.pop((y,x))

answer = 0
for y in range(N):
    for x in range(N):
        student = placement[y][x]
        like_cnt = 0
        for dir in range(DIRECTION):
            ny, nx = y + direct[dir][Y], x + direct[dir][X]
            if 0 <= ny < N and 0 <= nx < N and placement[ny][nx] and placement[ny][nx] in student_info[student]:
                like_cnt += 1
        if like_cnt:
            answer += 10**(like_cnt-1)
print(answer)