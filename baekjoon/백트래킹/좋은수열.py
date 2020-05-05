import sys
sys.stdin=open("좋은수열.txt","r")

def dfs(index, prev, result):
    global isEnd
    if index==N:
        print(''.join(map(str, result)))
        isEnd = True
        return
    for i in range(1,4):
        if i==prev: continue
        else:
            result.append(i)
            if index==0 or index==1:
                dfs(index+1,i,result)
                if isEnd:
                    return
            else:

                for j in range(2,len(result)):
                    isFail = False
                    for idx in range(len(result)-j):
                        if result[idx:idx+j]==result[idx+1:idx+j+1]:
                            isFail=True
                            break
                    if isFail:
                        break
                    isFail=False
                    if len(result)>=(2*j):
                        for idx in range(len(result)-j):
                            if result[idx:idx+j]==result[idx+j:idx+2*j]:
                                isFail=True
                                break
                    if isFail:
                        break
                else:
                    dfs(index + 1, i, result)
                    if isEnd:
                        return
            result.pop()

N = int(input())
result = []
isEnd = False
dfs(0,0,result)