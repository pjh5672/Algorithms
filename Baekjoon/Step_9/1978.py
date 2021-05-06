import math

N = int(input())
numbers = list(map(int, input().split()))
count = 0

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

for num in numbers:
    if is_prime(num):
        count += 1

print(count)

