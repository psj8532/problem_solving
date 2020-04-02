# result=4+True+False+5
# print(result)
# print(3 and 5)
# try:
#     num='abcd'
#     100/int(num)
# except Exception:
#     print('에러가 발생했습니다.')
# except ValueError:
#     print('에러가 발생했습니다.')
# finally:
#     print('완료되었습니다.')

import copy
list1=[3,'a','b']
list2=[1,2,list1]

list3=list1[:]
list4=copy.copy(list2)
list5=copy.deepcopy(list2)
list4[2]=5
print(list2[2])

# print(-3**2+3)

# sample_dict={}
# for i in enumerate(range(4)):
#     sample_dict[i[0]]=i[1]
#
# print(sum(sample_dict.values()))

# def fib(n):
#     if n==1:
#         print(10)
#     if n==0:
#         print(100)
#     if n==0 or n==1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# print(fib(4))

# word='python'
# indexing=word[3:8]
# print(indexing)

