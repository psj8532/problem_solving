def push_button(curr, dest):
    return abs(curr - dest)

CURRENT_CHANNEL, MAX_CHANNEL = 100, 1000000
N = int(input())
M = int(input())
if M: broken_buttons = list(input().split())
else: broken_buttons = []

answer = push_button(CURRENT_CHANNEL, N)

for channel in range(MAX_CHANNEL):
    channel = str(channel)
    channel_size = len(channel)
    if channel_size > 1 and channel[0] == '0': continue
    cnt = channel_size
    for ch in channel:
        if ch in broken_buttons:
            break
    else:
        answer = min(answer, cnt + push_button(int(channel), N))
print(answer)
