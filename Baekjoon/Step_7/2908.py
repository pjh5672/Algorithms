two_nums = list(map(str, input().split()))

rev_two_nums = []
for num in two_nums:
    temp = str()
    for v in reversed(num):
        temp += v
    rev_two_nums.append(int(temp))

print(max(rev_two_nums))