N = int(input())

def hanoi(n,f,t,s):
    if n == 1:
        # print('{} {}'.format(f,t))
        result.append((f,t))
        return
    hanoi(n-1,f,s,t)
    # print('{} {}'.format(f,t))
    result.append((f,t))
    hanoi(n-1,s,t,f)

result = []
hanoi(N,1,3,2)
print(len(result))
for row in result:
    print(*row)


# 원하는 번호의 원판을 목적지로 이동해야함
# 원하는 번호-1 번호판부터 1까지를 서브로 옮겨놔야함
# 원하는 번호판을 목적지에 가져다 놓음
# 서브에 있던 원하는번호-1~1까지를 목적지로 다시 가져와야함