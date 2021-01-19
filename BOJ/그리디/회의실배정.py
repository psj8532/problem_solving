N = int(input())
reservation = [list(map(int,input().split())) for _ in range(N)]
reservation.sort(key=lambda x:(x[1],x[0]))
end = -1
answer = 0
for s,e in reservation:
    if s >= end:
        answer += 1
        end = e
print(answer)
