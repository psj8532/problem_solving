def dfs(h,m,e,matrix,check,result):
    if h == e:
        if check:
            result.append(1)
        return
    else:
        if h not in matrix:
            return
        for n in matrix[h]:
            if n == m:
                check = True
            dfs(n, m, e, matrix, check, result)


def solution(depar, hub, dest, roads):
    answer = -1
    result = []
    adj = dict()
    for i in range(len(roads)):
        if roads[i][0] in adj:
            adj[roads[i][0]].append(roads[i][1])
        else:
            adj[roads[i][0]] = [roads[i][1]]
    dfs(depar,hub,dest,adj,False,result)
    answer = len(result)
    answer %= 10007
    if len(result) == 0: answer = 0
    return answer

ex1 = "SEOUL","DAEGU","YEOSU",[["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]
ex2 = "ULSAN","SEOUL","BUSAN",[["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]
print(solution(*ex2))