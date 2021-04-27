N = int(input())
assert N < 101
sum_num = 0
nums = str(input())
nums = nums[:N]

for i in nums:
    sum_num += int(i)

print(sum_num)
    