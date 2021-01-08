import copy

def solution(key, lock):
    answer = False
    def check(lst):
        k, l = len(lst), len(lock)
        for ki in range(-k+1,l):
            for kj in range(-k+1,l):
                temp = [[0]*l for _ in range(l)]
                # 열쇠 맞춰보기
                for i in range(l):
                    for j in range(l):
                        if ki <= i < ki + k and kj <= j < kj + k:
                            temp[i][j] += lst[i-ki][j-kj] + lock[i][j]
                        else:
                            temp[i][j] += lock[i][j]
                # 확인
                cnt = 0
                for i in range(l):
                    for j in range(l):
                        if temp[i][j] == 1:
                            cnt += 1
                if cnt == l**2:
                    return True
        return False

    rotate_cnt = 0
    while not answer and rotate_cnt < 4:
        # 제자리
        if check(key):
            answer = True
            break
        # 회전
        if rotate_cnt == 3: break
        t = [[0]*len(key) for _ in range(len(key))]
        i = 0
        for lst in zip(*key):
            for j in range(len(key)):
                t[i][j] = lst[len(key)-1-j]
            i += 1
        key = copy.deepcopy(t)
        rotate_cnt += 1
    return answer

# key	lock	result
ex1 = [[[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]]	# true
ex2 = [[[0,0,0],[0,1,0],[1,0,0]], [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,0,1]]] # true
ex3 = [[[0,1,0],[0,0,0],[1,0,0]], [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]]
ex4 = [[[0,0,0],[0,0,0],[0,1,0]], [[0,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]]
ex5 = [[[0,0,0],[0,0,0],[0,1,0]], [[1,1,1],[1,1,1],[1,1,0]]]
ex6 = [[[1,0,0],[0,0,0],[0,0,0]], [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,0]]]
print(solution(*ex6))