# # 13:43 ~ 14:50
# def solution(n):
#     def convert_bit(num):
#         temp = num
#         lst = []
#         while temp>1:
#             r = temp % 2
#             lst.append(r)
#             temp //= 2
#         lst.append(temp)
#         return lst
#
#     def convert_num(lst):
#         total = 0
#         for idx,c in enumerate(lst):
#             if c == 1:
#                 total += 2**idx
#         return total
#
#     nums = convert_bit(n)
#     start = nums.index(1)
#     for i in range(start+1,len(nums)):
#         if not nums[i]:
#             nums[i] = 1
#             nums[i-1] = 0
#             cnt = 0
#             for j in range(i-1):
#                 if nums[j]:
#                     cnt += 1
#                     nums[j] = 0
#             for j in range(cnt):
#                 nums[j] = 1
#             break
#     else:
#         cnt = 0
#         for i in range(start+1,len(nums)):
#             if nums[i]:
#                 cnt += 1
#         nums = [1,0] + nums[1:]
#         nums.reverse()
#         for i in range(cnt,len(nums)-2):
#             if i < cnt:
#                 nums[i] = 1
#             else:
#                 nums[i] = 0
#
#     return convert_num(nums)

def solution(n):
    cnt = bin(n).count('1')
    for num in range(n+1,1000001):
        if bin(num).count('1') == cnt:
            return num

ex1 = 78
ex2 = 15
ex3 = 5
ex4 = 2
ex5 = 14 # 19
print(solution(ex4))