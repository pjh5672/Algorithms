T = int(input())

for _ in range(T):
    x, y = map(int, input().split())
    dist = y - x
    cnt = 1

    while True:
        if cnt ** 2 <= dist < (cnt+1) ** 2:
            break
        cnt += 1
    if cnt ** 2 == dist:
        print((cnt * 2)-1)
    elif cnt ** 2 < dist <= cnt**2 + cnt:
        print(cnt * 2)
    else:
        print((cnt * 2) + 1)