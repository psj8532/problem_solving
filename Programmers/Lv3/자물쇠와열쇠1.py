import copy

def solution(key, lock):
    KEY_SIZE, LOCK_SIZE = len(key), len(lock)
    L = add_space = (KEY_SIZE - 1)
    MATRIX_SIZE = (2 * add_space) + LOCK_SIZE
    def check(ky, kx, nk):
        matrix = [[0] * MATRIX_SIZE for _ in range(MATRIX_SIZE)]
        for i in range(KEY_SIZE):
            for j in range(KEY_SIZE):
                matrix[ky+i][kx+j] += nk[i][j]
        for i in range(LOCK_SIZE):
            for j in range(LOCK_SIZE):
                if matrix[L+i][L+j] + lock[i][j] != 1: return False
        return True

    def rotate(o):
        n = [[0] * KEY_SIZE for _ in range(KEY_SIZE)]
        for i in range(KEY_SIZE):
            for j in range(KEY_SIZE):
                n[j][KEY_SIZE-1-i] = o[i][j]
        return n

    rotation = 0
    new_key = copy.deepcopy(key)

    while rotation < 4:
        for ki in range(MATRIX_SIZE - add_space):
            for kj in range(MATRIX_SIZE - add_space):
                if check(ki, kj, new_key): return True

        new_key = rotate(new_key)
        rotation += 1
    return False

# key	lock	result
ex1 = ([[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]])	#true
ex2 = [[[0,0,0],[0,1,0],[1,0,0]], [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,0,1]]]
print(solution(*ex2))