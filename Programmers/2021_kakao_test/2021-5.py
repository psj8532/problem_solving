from _collections import deque


def change_sec(time):
    h, m, s = time.split(':')
    h,m,s = int(h)*3600,int(m)*60,int(s)
    s = h + m + s
    return s


def change_time(s_time):
    temp = s_time
    h = format(temp//3600,'02')
    temp %= 3600
    m = format(temp//60,'02')
    temp %= 60
    s = format(temp,'02')
    text = h + ':' + m + ':' + s
    return text


def solution(play_time, adv_time, logs):
    answer = ''
    new_logs = []
    log_count = dict()
    stime = 0
    npt = change_sec(play_time)
    at = change_sec(adv_time)
    if npt == at:
        answer = '00:00:00'
        return answer
    for word in logs:
        temp_list = []
        temp = list(word.split('-'))
        for idx in range(2):
            s = change_sec(temp[idx])
            temp_list.append(s)
        new_logs.append(temp_list)
    new_logs.sort(key=lambda x:x[1])
    deq = deque()
    for i in new_logs:
        deq.append(i)

    while deq:
        st,et = deq.popleft()
        sum = 0
        for i in range(len(new_logs)):
            if new_logs[i][0] <= st <= new_logs[i][1] and new_logs[i][1] <= st+at:
                sum = sum + new_logs[i][1] - st
            elif new_logs[i][0] >= st and new_logs[i][1] <= st+at:
                sum = sum + new_logs[i][1] - new_logs[i][0]
            elif st <= new_logs[i][0] <= st+at and new_logs[i][1] >= st+at:
                sum = sum + st + at - new_logs[i][0]
        log_count[st] = sum

    max_key = 0
    max_val = 0
    for k,v in log_count.items():
        if v > max_val:
            max_val = v
            max_key = k
        elif v == max_val:
            if k < max_key:
                max_key = k
    stime = max_key
    answer = change_time(stime)
    return answer

ex1 = ["02:03:55","00:14:15",["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]]
ex2 = ["99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]]
ex3 = ["50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]]
print(solution(*ex2))