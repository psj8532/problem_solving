import sys
import time
sys.stdin = open("자동차경주대회.txt", "r")
stime = time.time()

def dfs(d,sum,idx,cnt):
    global result_cnt,min,count,isEnd
    if idx == workshop_cnt and sum < min:
        count += 1
        temp = a[:]
        result.append(temp)
        min = sum
        result_cnt = cnt
    else:
        if isEnd: return
        td = d
        for j in range(idx+1,workshop_cnt,1):
            td += distance_list[j]
            # for n in range(idx+1,j+1):
            #     td += distance_list[n]
            if sum + workshop_list[j] < min and td <= distance:
                a.append(j+1)
                dfs(0,sum+workshop_list[j],j,cnt+1)
                a.pop()
            elif td > distance:
                break
        else:
            # td = d
            # for n in range(idx+1,workshop_cnt+1):
            #     td += distance_list[n]
            td += distance_list[workshop_cnt]
            if td <= distance:
                if not cnt:
                    isEnd = True
                dfs(0,sum,workshop_cnt,cnt)


distance = int(input())
workshop_cnt = int(input())
distance_list = list(map(int,input().split()))
workshop_list = list(map(int,input().split()))
a = []
result = []
min = 9876543210
result_cnt = 0
count = -1
isEnd = False
dfs(0,0,-1,0)
print(min)
if result_cnt:
    print(result_cnt)
    print(*result[count])
else:
    print(0)

print('time: {}'.format(time.time()-stime))