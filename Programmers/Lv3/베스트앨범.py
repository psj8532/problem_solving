# 16:36 ~
def solution(genres, plays):
    answer = []
    music, N = {}, len(genres)
    for idx in range(N):
        genre, play = genres[idx], plays[idx]
        if genre in music:
            music[genre].append([idx, play])
        else:
            music[genre] = [[idx, play]]
    genre_lst = []
    for k in music:
        total = 0
        for i, cnt in music[k]:
            total += cnt
        genre_lst.append([k, total])
    genre_lst.sort(reverse=True, key=lambda x:x[1])

    for genre, _ in genre_lst:
        music[genre].sort(reverse=True, key=lambda x: (x[1], -x[0]))
        for i in range(min(len(music[genre]), 2)):
            answer.append(music[genre][i][0])
    return answer

ex1 = (["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]) # [4, 1, 3, 0]
print(solution(*ex1))