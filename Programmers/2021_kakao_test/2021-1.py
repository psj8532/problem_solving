#14:00 ~ 14:37
def remove_ch(s,p):
    while p:
        s.pop(p.pop())
    return s

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    arr = list(new_id)
    posi = []
    print(arr)
    #2
    for i in range(len(arr)):
        if not arr[i].isalpha() and not arr[i].isdigit() and arr[i] != '.' and arr[i] != '_' and arr[i] != '-':
            posi.append(i)
    arr = remove_ch(arr,posi)
    print(arr)
    #3
    posi = []
    for i in range(1,len(arr)):
        if arr[i-1] == '.' and arr[i] == '.':
            posi.append(i)
    arr = remove_ch(arr,posi)
    print(arr)
    #4
    posi = []
    if len(arr) != 0 and arr[len(arr)-1] == '.': arr.pop()
    if len(arr) != 0 and arr[0] == '.': arr.pop(0)
    print(arr)
    #5
    if len(arr) == 0: arr.append('a')
    print(arr)
    #6
    if len(arr) > 15:
        arr = arr[:15]
        if arr[14] == '.': arr.pop()
    print(arr)
    #7
    if len(arr) <= 2:
        cnt = len(arr)
        while cnt < 3:
            arr.append(arr[len(arr)-1])
            cnt += 1
    print(arr)
    answer = "".join(arr)
    return answer


ex1 = "123_.def"
print(solution(ex1))