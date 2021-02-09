N, M = map(int,input().split())
opcodes = [list(map(int,input().split())) for _ in range(M)]
trains, visited = [0]*N, []
answer, LIMIT = N, 20
for opcode in opcodes:
    if opcode[0] == 1 or opcode[0] == 2:
        n = opcode[2] - 1
    c, t = opcode[0], opcode[1] - 1
    # 1: 1 or / 2: 0 and / 3: <<= / 4: >>=
    # 비트의 맨 뒤를 기차의 맨 앞이라고 가정
    if c == 1:
        trains[t] = trains[t] | 1<<n
    elif c == 2:
        if trains[t] < (1<<n): continue
        b = bin(trains[t])
        temp = '0b' + '1'*(len(b)-n-1) + '0' + '1'*n

        # b[-(n+1)] = int(b[-(n+1)]) & temp
        trains[t] = int(bin(int(b, 2) & int(temp, 2)),2)
    elif c == 3:
        trains[t] <<= 1
        if len(bin(trains[t])) > LIMIT:
            trains[t] = int(bin(trains[t])[3:], 2)
    else:
        trains[t] >>= 1

for train in trains:
    if train in visited: answer -= 1
    else:
        visited.append(train)
print(answer)

# N, M = map(int,input().split())
# opcodes = [list(map(int,input().split())) for _ in range(M)]
# trains, visited = [[0]*20 for _ in range(N)], set()
# LIMIT = N
# for opcode in opcodes:
#     if opcode[0] == 1 or opcode[0] == 2:
#         n = opcode[2] - 1
#     c, t = opcode[0], opcode[1] - 1
#     if c == 1:
#         trains[t][n] = 1
#     elif c == 2:
#         trains[t][n] = 0
#     elif c == 3:
#         trains[t].insert(0,0)
#         if len(trains[t]) > LIMIT:
#             trains[t].pop()
#     else:
#         trains[t].pop()
#         trains[t].append(0)
# for train in trains:
#     visited.add(tuple(train))
# for row in trains:
#     print(*row)