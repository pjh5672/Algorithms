N = int(input())
a, b = 3, 5
bag = 0

while N >= 0:
    if N % b == 0:
        bag += (N // b)
        print(bag)
        break
    N -= a
    bag += 1
else:
    print(-1)