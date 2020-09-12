# 14:39 ~ 16:30
from itertools import combinations


def solution(orders, course):
    answer = []
    temp_list = []
    order_dict = {course[i]:[] for i in range(len(course))}
    for i in range(len(orders)):
        for num in course:
            if num <= len(orders[i]):
                comb = list(combinations(orders[i],num))
                for j in range(len(comb)):
                    word = []
                    for idx in range(num):
                        word.append(comb[j][idx])
                    temp = sorted(word)
                    order_dict[num].append("".join(temp))
    for num in course:
        count_dict = dict()
        for i in range(len(order_dict[num])):

            if order_dict[num][i] in count_dict:
                count_dict[order_dict[num][i]] += 1
            else:
                count_dict[order_dict[num][i]] = 1
        if count_dict:
            max_value = max(count_dict.values())
            if max_value > 1:
                max_key = [temp_list.append(k) for k,v in count_dict.items() if v == max_value]
    answer = sorted(temp_list)
    return answer


ex1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]
ex2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]
ex3 = ["XYZ", "XWY", "WXA"],[2,3,4]
print(solution(*ex3))