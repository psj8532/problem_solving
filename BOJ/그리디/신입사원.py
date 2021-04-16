T = int(input())
for tc in range(T):
    N = int(input())
    document = [0] * (N + 1)
    answer = 0
    for idx in range(N):
        doc_ranking, int_ranking = map(int,input().split())
        document[doc_ranking] = int_ranking

    top_interview = document[1]

    for i in range(1, N + 1):
        if (document[i] <= top_interview):
            answer += 1
            top_interview = document[i]

    print(answer)