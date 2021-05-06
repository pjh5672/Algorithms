import math
M = int(input())
N = int(input())

def is_prime(num):
    answer = True
    if num == 1:
        answer = False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            answer = False
            break
    return answer

prime_nums = []
for num in range(M, N+1):
    if is_prime(num):
        prime_nums.append(num)

if len(prime_nums) == 0:
    print(-1)
else:
    print(sum(prime_nums))
    print(min(prime_nums))

