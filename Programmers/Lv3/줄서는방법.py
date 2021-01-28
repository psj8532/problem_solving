def solution(n, k):
    answer = []
    lst = [i for i in range(1, n+1)]
    nums = n-1
    while nums >= 0:
        if not nums: ns = 0
        else:
            ns = 1
            for i in range(nums,0,-1):
                ns *= i
        idx = 1
        while ns and ns * idx < k:
            idx += 1
        idx -= 1
        num = lst.pop(idx)
        answer.append(num)
        nums -= 1
        k -= ns * idx
    return answer

ex1 = (3, 5)
print(solution(*ex1))