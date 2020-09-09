def get_array(temp):
    result = []
    for i in range(0,len(temp)-1):
        if temp[i].isalpha() and temp[i+1].isalpha():
            s = temp[i].upper() + temp[i+1].upper()
            result.append(s)
    return result


def solution(str1, str2):
    answer = 0
    str_list = []
    intersection = []
    union = []
    str_list.append(get_array(str1))
    str_list.append(get_array(str2))
    visited = [False]*len(str_list[1])
    for i in range(len(str_list[0])):
        for j in range(len(str_list[1])):
            if str_list[0][i] == str_list[1][j] and not visited[j]:
                intersection.append(str_list[0][i])
                visited[j] = True
                break
    visited = [False]*len(str_list[1])
    for i in range(len(str_list[0])):
        union.append(str_list[0][i])
        for j in range(len(str_list[1])):
            if str_list[0][i] == str_list[1][j] and not visited[j]:
                visited[j] = True
                break
    for i in range(len(str_list[1])):
        if not visited[i]:
            union.append(str_list[1][i])
    if len(union) == 0:
        answer = 65536
    else:
        answer =  int(len(intersection)/len(union)*65536)
    return answer