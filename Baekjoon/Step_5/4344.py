C = int(input())
N_list = []
scores_list = []

for _ in range(C):
    T = [item for item in map(int, \
        input().split())]
    N = T[0]
    scores = T[1:]
    N_list.append(N)
    scores_list.append(scores)

for idx in range(C):
    N = N_list[idx]
    scores = scores_list[idx]
    avg = sum(scores)/N
    cnt = [1 for score in scores \
        if score > avg]
    print("{:.3f}%".format(sum(cnt)/N * 100))
    