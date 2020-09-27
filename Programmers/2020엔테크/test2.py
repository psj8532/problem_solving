#1
# def dfs(cnt,m,n,a,D):
#     if cnt == n:
#         for r in range(2):
#             for c in range(n):
#                 if not m[r][c]:
#                     return
#         a.append(1)
#     else:
#         for i in range(2):
#             for j in range(n):
#                 if not cnt or not m[i][j]:
#                     m[i][j] = 1
#                     for dir in range(4):
#                         ny,nx = i+D[dir][0],j+D[dir][1]
#                         if 0 <= ny < 2 and 0 <= nx < n and not m[ny][nx]:
#                             m[ny][nx] = 1
#                             dfs(cnt+1,m,n,a,D)
#                             m[ny][nx] = 0
#                     m[i][j] = 0
#                     if not cnt: return
# def solution(N):
#     answer = 0
#     ans = []
#     matrix = [[0]*N for _ in range(2)]
#     direct = [(-1,0),(0,1),(1,0),(0,-1)]
#     matrix[0][0] = 1
#     dfs(0,matrix,N,ans,direct)
#     answer = ans.count(1)
#     answer //= 2
#     return answer
#
#
# print(solution(3))

#2
# def solution(N):
#     answer = 0
#     if N >= 3:
#         answer += solution(N-1)
#         answer += solution(N-2)
#     elif N == 2:
#         answer += 2
#     elif N == 1:
#         answer += 1
#
#     return answer

#3
def solution(N):
    answer_list = [0] * 46
    answer_list[1] = 1
    answer_list[2] = 2
    for idx in range(3, 46):
        answer_list[idx] = answer_list[idx-1] + answer_list[idx-2]

    return answer_list[N]