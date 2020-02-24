# 퇴사 # 18:10

import sys
sys.stdin=open("14501.text","r")
def Schedule(now,n):
    global val, result
    if now < n and now+data[now][0]<=n+1:#다음게 n을 넘어가면 안됨
        val += data[now][1]
    elif now < n and now+data[now][0]>n+1:
        if val > result:
            result = val
        return
    elif now==n:
        if data[n][0]<=1:
            val += data[now][1]
        else:
            if val > result:
                result = val
            return
    elif now>=n+1:
        if val > result:
            result = val
        return

    next = now + data[now][0]
    if next==n+1:
        Schedule(next,n)
    else:
        for idx in range(next,n+1):
            Schedule(idx,n)
            if idx<n:
                if idx + data[idx][0] <= n + 1:  # 다음게 n을 넘어가면 안됨
                    val -= data[idx][1]
                elif idx + data[idx][0] > n + 1:
                    return
            elif idx == n and data[n][0]<=1:
                val -= data[idx][1]
    return

n = int(input())
data = [[0]*2]
for _ in range(n):
    data.append(list(map(int,input().split())))
result=0
val=0
for i in range(1,n+1):
    Schedule(i,n)
print(result)