def solution(record):
    answer = []
    new_record = []
    result = []
    for _ in range(len(record)):
        new_record.append((record[_].split()))

    idx_dict = dict()
    name_dict = dict()

    for i in range(len(new_record)):
        if new_record[i][0] == "Leave":
            code, user = new_record[i][0], new_record[i][1]
            # 나가는 것이므로 무조건 들어온적이 있음
            idx_dict[user].append(i)
            result.append(name_dict[user])
        else:
            code, user, name = new_record[i][0], new_record[i][1], new_record[i][2]
            result.append(name)
            if code == 'Enter':
                if user in name_dict:
                    idx_dict[user].append(i)
                    if name_dict[user] != name:
                        for v in idx_dict[user]:
                            result[v] = name
                        name_dict[user] = name

                else: # 처음 들어옴
                    name_dict[user] = name
                    idx_dict[user] = [i]

            else:
                # 변경도 무조건 들어온 적이 있고, 기존의 닉네임과 무조건 다름
                idx_dict[user].append(i)
                for v in idx_dict[user]:
                    result[v] = name
                name_dict[user] = name

    for i in range(len(result)):
        name = result[i]
        if new_record[i][0] == 'Change': continue
        elif new_record[i][0] == 'Enter':
            answer.append("{}님이 들어왔습니다.".format(name))
        elif new_record[i][0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(name))

    return answer


ex1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(ex1))