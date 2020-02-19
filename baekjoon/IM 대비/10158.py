#개미   #17:28
import sys
sys.stdin = open("10158.text","r")

# def DoTurn(y,x,w,h):
#     if y == 0 or y == h or x == 0 or x == w:
#         return True
#     else:
#         return False

w, h = map(int,input().split())
posi = list(map(int,input().split()))
t = int(input())
y = posi[1]
x = posi[0]
dy = [1, 1, -1, 1]
dx = [1, -1, -1, -1]

dir = 0
time=0

while time < t:
    time+=1
    dir %= len(dy)
    y += dy[dir]
    x += dx[dir]
    # if DoTurn(y,x,w,h):
    #     dir+=1
    if y == 0 or y == h or x == 0 or x == w:
        dir += 1

print('{} {}'.format(x, y))