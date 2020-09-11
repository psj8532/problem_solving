#21:05 ~ 21:55
def binary_convert(n,a,a1):
    for i in range(n):
        number = a1[i]
        temp = []
        if number == 0:
            pass
        elif number == 1:
            temp.append(1)
        else:
            while number != 1:
                if number // 2 == 1:
                    temp.append(number%2)
                    number //= 2
                    temp.append(1)
                else:
                    temp.append(number%2)
                    number //= 2
        cnt = len(temp)
        while cnt != n:
            temp.append(0)
            cnt += 1
        temp.reverse()
        for j in range(n):
            if a[i][j] or temp[j]:
                a[i][j] = 1
    return a


def solution(n, arr1, arr2):
    answer = []
    arr = [[0]*n for _ in range(n)]
    arr = binary_convert(n,arr,arr1)
    arr = binary_convert(n,arr,arr2)
    for r in range(n):
        for c in range(n):
            if arr[r][c]:
                arr[r][c] = '#'
            else:
                arr[r][c] = ' '
    for r in range(n):
        answer.append("".join(arr[r]))
    print(answer)
    return answer