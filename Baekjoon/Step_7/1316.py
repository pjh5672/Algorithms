N = int(input())
num_group = 0

for _ in range(N):
    word = input().lower()

    for i in range(len(word)):
        if i != len(word) - 1:
            if word[i] == word[i+1]:
                pass
            elif word[i] in word[i+1:]:
                break
        else:
            num_group += 1

print(num_group)
        