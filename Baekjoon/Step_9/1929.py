import math

M,N = list(map(int, input().split()))

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


for num in range(M, N+1):
    if is_prime(num):
        print(num)