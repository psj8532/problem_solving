def solution(board):
    answer = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j])+1
                answer = max(answer, board[i][j])
    if len(board) == 1 or len(board[0]) == 1:
        for r in range(len(board)):
            answer = max(answer, max(board[r]))
        return answer
    return answer**2

ex1 = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	# 9
ex2 = [[0,0,1,1],[1,1,1,1]]	# 4
ex3 = [[0,0,0,0],[0,1,1,0],[1,1,1,1],[1,1,1,0]]
ex4 = [[0]*1000 for _ in range(1000)]
ex5 = [[1,1,1,1]]
ex6 = [[1],[0],[0]]
print(solution(ex1))
