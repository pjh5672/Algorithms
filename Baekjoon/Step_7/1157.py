word = input().upper()

unique_char = list(set(word))
cnt_list = []

for x in unique_char:
    cnt = word.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print("?")
else:
    print(unique_char[cnt_list.index(max(cnt_list))])