N = int(input())
score = [item for item in map(int, input().split())]

max_score = max(score)
new_score = [100*item/max(score) for item in score]

new_sum = 0
for score in new_score:
    new_sum += score

print(new_sum/N)