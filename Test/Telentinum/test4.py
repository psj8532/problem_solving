# def isPrime(n):
#     # Write your code here
#     matrix = [0] * (n+1)
#     val = int(n**0.5)
#     for i in range(2,n+1):
#         for j in range(2,val+1):
#             if i != j and not i %j:
#                 break
#         else:
#             matrix[i] = i
#     answer = 0
#     for i in range(len(matrix)):
#         if matrix[i]:
#             answer = matrix[i]
#     if answer == n:
#         return 1
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return i
#
# print(isPrime(37961921))

def isPrime(n):
    # Write your code here
    if n == 2: return 1
    for i in range(2,n):
        if n % i == 0: #소수아님
            answer = i
            break
    else:
        answer = 1
    return answer


print(isPrime(37961921))