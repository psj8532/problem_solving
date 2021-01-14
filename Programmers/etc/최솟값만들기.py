def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer

ex1 = [[1, 4, 2], [5, 4, 4]]	# 29
ex2 = [[1,2], [3,4]]	# 10
ex3 = [i+1 for i in range(1000)]
ex4 = [i+1 for i in range(1000)]
ex5 = [[1,3,4,5,6],[10,5,4,3,1]]
print(solution(ex3,ex4))