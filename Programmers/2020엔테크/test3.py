def solution(histogram):
    answer = 0
    for i in range(len(histogram)-2):
        for j in range(i+2,len(histogram)):
            width = j-i-1
            if histogram[i] < histogram[j]:
                height = histogram[i]
            else:
                height = histogram[j]
            val = width * height
            if val > answer:
                answer = val
    return answer

ex1 = [2, 2, 2, 3]
ex2 = [6, 5, 7, 3, 4, 2]
print(solution(ex2))