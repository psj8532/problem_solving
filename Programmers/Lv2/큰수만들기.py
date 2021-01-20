# 12:42 ~
# def solution(number, k):
#     answer = ''
#     numbers = list(map(int,str(number)))
#     cnt = 0
#     isEnd = False
#     while cnt < k and not isEnd:
#         print('--------')
#         print('numbers: ', *numbers)
#         isEnd = True
#         if len(numbers) > 1 and numbers[0] < numbers[1]:
#             numbers.pop(0)
#             isEnd = False
#             cnt += 1
#             continue
#         for i in range(1,len(numbers)-1):
#             if numbers[i-1] > numbers[i] and numbers[i] < numbers[i+1]:
#                 numbers.pop(i)
#                 cnt += 1
#                 isEnd = False
#                 break
#         if not isEnd:
#             continue
#
#         if len(numbers) > 1 and numbers[-1] < numbers[-2]:
#             numbers.pop(len(numbers)-1)
#             cnt += 1
#
#     while cnt < k:
#         print('--------')
#         print('numbers: ', *numbers)
#         for i in range(len(numbers)-1,0,-1):
#             if numbers[i-1] > numbers[i]:
#                 numbers.pop(i)
#                 cnt += 1
#                 break
#         else:
#             numbers.pop(0)
#             cnt += 1
#     answer = "".join(list(map(str,numbers)))
#     return answer


def solution(number, k):
    answer = ''
    numbers = list(map(int,number))
    max_idx = -1
    for idx in range(len(numbers)-k):
        max_val = 0
        for s in range(max_idx+1,idx+k+1):
            if numbers[s] > max_val:
                max_val = numbers[s]
                max_idx = s
        answer += str(max_val)

    return answer

# number	k	return
ex1 = ["1924", 2]	# 94
ex2 = ["1231234", 3]	# 3234
ex3 = ["4177252841", 4]	# 775841
ex4 = [42315697, 7]
ex5 = [3044, 2]
ex6 = [87654321, 3]
ex7 = [111199,3]
ex8 = [99765,1]
print(solution(*ex3))