import math

T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    count = 0

    num = math.floor(math.sqrt(dist))
    num_square = num ** 2
    increase_num = math.sqrt(num_square)

    if dist > num_square + increase_num:
        count = 2 * num + 1
    elif dist > num_square and dist <= num_square + increase_num:
        count = 2 * num
    elif dist == num_square:
        count = 2 * num - 1
    
    if dist <= 3:
        count = dist
    
    print(count)