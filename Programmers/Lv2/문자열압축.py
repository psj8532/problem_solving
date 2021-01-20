# 18:53 ~ 19:52
def solution(s):
    answer = 1001
    for cnt in range(1,len(s)+1):
        c_lst = []
        s_lst = []
        for start in range(0,len(s),cnt):
            end = start + cnt
            word = s[start:end]
            c_lst.append(word)

        for i in range(len(c_lst)):
            if i == 0:
                cnt = 1
            elif c_lst[i-1] == c_lst[i]:
                cnt += 1
            else:
                if cnt != 1:
                    s_lst.append(str(cnt))
                s_lst.append(c_lst[i-1])
                cnt = 1
        else:
            if cnt != 1:
                s_lst.append(str(cnt))
            s_lst.append(c_lst[-1])

        s_str = "".join(s_lst)
        answer = min(answer,len(s_str))

    return answer

# s	result
ex1 = "aabbaccc"	# 7
ex2 = "ababcdcdababcdcd"	# 9
ex3 = "abcabcdede"	# 8
ex4 = "abcabcabcabcdededededede"	# 14
ex5 = "xababcdcdababcdcd"	# 17
ex6 = 'a' # 1
print(solution(ex6))