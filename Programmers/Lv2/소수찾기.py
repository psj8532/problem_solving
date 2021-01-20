import math

def solution(numbers):
    answer = 0
    def perm(index,end):
        if index == end:
            temp = a[:]
            s.append(temp)
        else:
            in_perm = [False] * len(numbers)

            for i in range(index):
                in_perm[a[i]] = True

            c = [0] * len(numbers)
            cnt = 0
            for i in range(len(numbers)):
                if not in_perm[i]:
                    c[cnt] = i
                    cnt += 1

            for i in range(cnt):
                a[index] = c[i]
                perm(index+1,end)
    s = []
    for i in range(1,len(numbers)+1):
        a = [0] * i
        perm(0,i)
    nums = []
    for lst in s:
        num = ''
        for n in lst:
            num += numbers[n]
        num = int(num)
        nums.append(num)
    max_val = max(nums)
    check = [0]*(max_val+1)
    check[0] = check[1] = 1
    target = math.sqrt(max_val)
    target = math.floor(target)
    for i in range(2,target+1):
        if not check[i]:
            for j in range(i+i,max_val+1,i):
                check[j] = 1
    nums = set(nums)
    while nums:
        val = nums.pop()
        if not check[val]: answer += 1

    return answer

ex1 = "17"
ex2 = "011"
print(solution(ex1))