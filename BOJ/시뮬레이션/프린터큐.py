T = int(input())
for tc in range(T):
    N, M = map(int,input().split())
    nums = list(map(int,input().split()))
    nnums = []
    for i,num in enumerate(nums):
        nnums.append([num,i])
    number,idx = nnums[M][0],nnums[M][1]
    cnt = 0
    while nnums:
        curr_num, curr_idx = nnums.pop(0)
        for i in range(len(nnums)):
            if nnums[i][0] > curr_num:
                nnums.append([curr_num, curr_idx])
                break
        else:
            cnt += 1
            if curr_num == number and curr_idx == idx: break
    print(cnt)
