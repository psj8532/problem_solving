def solution(n, customers):
    def cal_time(cur, ing):
        mon = int(cur[0:2])
        day = int(cur[3:5])
        h = int(cur[6:8])
        m = int(cur[9:11])
        s = cur[12:]
        if ing[0] == '0':
            ing = int(ing[1])
        else:
            ing = int(ing)
        m += ing
        if m > 60:
            m = m % 60
            h += 1
            if h > 23:
                h = h % 24
                day += 1
                if day > 28 and mon == 2:
                    mon += 1
                    day = day % 28
                elif day > 30 and mon in (4, 6, 9, 11):
                    mon += 1
                    day = day % 30
                elif day > 31 and mon in (1, 3, 5, 7, 8, 10, 12):
                    mon += 1
                    day = day % 31

        def plus_zero(word):
            if len(word) == 1:
                return '0' + word
            else:
                return word

        mon = plus_zero(str(mon))
        day = plus_zero(str(day))
        h = plus_zero(str(h))
        m = plus_zero(str(m))

        return mon + '/' + day + ' ' + h + ':' + m + ':' + s

    history = ['00/00 00:00:00'] * n
    res = [0] * n
    for customer in customers:
        target = '12/31 99:99:99'
        target_idx = -1
        cur = customer[:-3]
        ing = customer[-3:]

        for idx, time in enumerate(history):
            if cur > time:
                if time < target:
                    target = time
                    target_idx = idx

        if target_idx >= 0:
            res[target_idx] += 1
            history[target_idx] = cal_time(cur, ing)
        else:
            target_idx = history.index(min(history))
            history[target_idx] = cal_time(history[target_idx], ing)
            res[target_idx] += 1

    return max(res)

ex1 = 3, ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]

print(solution(*ex1))