def solution(dartResult):
    answer = 0
    matrix = []
    num = ''
    for ch in dartResult:
        if ch.isdigit():
            num += ch
        elif ch.isalpha():
            matrix.append(num)
            matrix.append(ch)
            num = ''
        else:
            matrix.append(ch)
    score = [0] * 3
    idx = 0
    for i in range(len(matrix)):
        if matrix[i].isdigit():
            score[idx] = int(matrix[i])
            idx += 1
        elif matrix[i] == 'S':
            continue
        elif matrix[i] == 'D':
            score[idx-1] = score[idx-1] ** 2
        elif matrix[i] == 'T':
            score[idx-1] = score[idx-1] ** 3
        elif matrix[i] == '*':
            if idx == 1:
                score[idx-1] *= 2
            else:
                score[idx-2] *= 2
                score[idx-1] *= 2
        elif matrix[i] == '#':
            score[idx-1] *= -1
    for number in score:
        answer += number

    return answer


ex1 = '1S2D*3T'
ex2 = '1D2S#10S'
ex3 = '1D2S0T'
ex4 = '1S*2T*3S'
ex5 = '1D#2S*3S'
ex6 = '1T2D3D#'
ex7 = '1D2S3T*'
print(solution(ex7))