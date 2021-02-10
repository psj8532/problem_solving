# 14:55 ~ 15:31
N = int(input())
S = int(input())
students = list(map(int,input().split()))
answer, pictures, recommend = [], [], [0] * 101
time = 0
for student in students:
    if recommend[student]:
        recommend[student] += 1
        for i in range(len(pictures)):
            if pictures[i][0] == student:
                pictures[i][1] += 1
                break
    else:
        if len(pictures) >= N:
            std, _, __ = pictures.pop(0)
            recommend[std] = 0
        pictures.append([student, 1, time])
        recommend[student] = 1
        time += 1
    pictures.sort(key=lambda x:(x[1],x[2]))
for i, v in enumerate(recommend):
    if not v: continue
    answer.append(i)
answer.sort()
print(*answer)