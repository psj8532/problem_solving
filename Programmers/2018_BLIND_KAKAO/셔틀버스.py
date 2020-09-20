def solution(n, t, m, timetable):
    answer = ''
    table = []
    for s in timetable:
        h,mm = int(s[0:2])*60,int(s[3:5])
        table.append(h+mm)
    table.sort()
    cnt = 0
    idx = 0
    while cnt < n:
        time = 540 + cnt * t
        num = 0
        for i in range(idx,len(table)):
            if num < m and table[i] <= time:
                num += 1
                idx = i
            else:
                idx = i
                break
        else:
            idx += 1
        cnt += 1
    if num < m:
        answer = time
    else:
        answer = table[idx-1]-1
    if answer >= 1440:
        answer = 1439
    h = answer // 60
    answer = answer - h * 60
    h = str(h).zfill(2)
    mm = str(answer).zfill(2)
    answer = h + ':' + mm
    return answer


ex1 = 1,1,5,['08:00', '08:01', '08:02', '08:03']
ex2 = 2,10,2,['09:10', '09:09', '08:00']
ex3 = 2,1,2,['09:00', '09:00', '09:00', '09:00']
ex4 = 1,1,5,['00:01', '00:01', '00:01', '00:01', '00:01']
ex5 = 1,1,1,['23:59']
ex6 = 10,60,45,['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']

print(solution(*ex2))