def solution(n, t, m, timetable):
    answer = ''
    table = []
    for s in timetable:
        h,m = int(s[0:2]),int(s[3:5])
        h = int(h)*60
        m += h
        table.append(m)
    table.sort()
    print(*table)
    return answer

print(solution(2,10,2,["09:10", "09:09", "08:00"]))