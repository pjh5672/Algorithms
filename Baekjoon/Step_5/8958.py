N = int(input())

for i in range(N):
    cnt = 1
    score = 0
    quiz_res = input()
    n_quiz = len(quiz_res)
    for j in range(n_quiz):
        if quiz_res[j] == 'O':
            score += cnt
            cnt += 1
        else:
            cnt = 1
    print(score)