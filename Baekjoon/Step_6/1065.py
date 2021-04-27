N = int(input())
num_hansu = 0
if N > 1000:
    N = 1000

for n in range(1, N+1):
    if n < 100:
        num_hansu += 1
    else:
        nums = list(map(int, str(n)))
        if (nums[0] - nums[1] == nums[1] - nums[2]):
            num_hansu += 1

print(num_hansu)