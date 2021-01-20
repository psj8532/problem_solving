# 12:41 ~ 13:50
def solution(arr):
    def divide(sy,ey,sx,ex,size):
        if size == 1:
            return [arr[sy][sx]]

        else:
            mid = size // 2
            check = arr[sy][sx]
            for i in range(sy,ey):
                for j in range(sx,ex):
                    if check != arr[i][j]:
                        temp = []
                        temp += divide(sy, sy+mid , sx, sx+mid, mid)
                        temp += divide(sy, sy+mid, sx+mid, ex, mid)
                        temp += divide(sy+mid, ey, sx, sx+mid, mid)
                        temp += divide(sy+mid, ey, sx+mid, ex, mid)
                        return temp
            else:
                return [check]


    start, end = 0, len(arr)
    answer = divide(start,end,start,end,len(arr))
    print(*answer)
    answer = "".join(map(str,answer))
    return [answer.count('0'), answer.count('1')]

ex1 = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
ex2 = [[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]
ex3 = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[0,1,1,0]]
print(solution(ex3))