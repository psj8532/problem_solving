pieces = list(map(int,input().split()))
def check(lst):
    val = 1
    for num in lst:
        if val == num: val += 1
        else: return False
    return True

while not check(pieces):
    for i in range(4):
        if pieces[i] > pieces[i+1]:
            pieces[i], pieces[i+1] = pieces[i+1], pieces[i]
            print(*pieces)