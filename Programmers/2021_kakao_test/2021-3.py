# 16:34 ~ 17:10 효율성은 하나도 통과 못함
def solution(info, query):
    answer = []
    new_info = []
    for word in info:
        temp = list(word.split(' '))
        new_info.append(temp)
    new_query = []
    for word in query:
        temp = list(word.split(' and '))
        tl = temp[len(temp)-1].split(' ')
        temp[len(temp)-1] = tl[0]
        temp.append(tl[1])
        new_query.append(temp)
    for i in range(len(new_query)):
        cnt = 0
        for j in range(len(new_info)):
            k = 0
            while k < 4:
                if new_query[i][k] == new_info[j][k] or new_query[i][k] == '-':
                    k += 1
                    if k == 4 and int(new_query[i][k]) <= int(new_info[j][k]):
                        cnt += 1
                else:
                    break
        answer.append(cnt)
    return answer



ex1 = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(*ex1))