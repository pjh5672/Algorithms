T = int(input())

for _ in range(T):
    H, W, N = list(map(int, input().split()))
    Y = N % H
    XX = (N // H) + 1 
    if Y == 0:
        Y = H
        XX -= 1
    print("{:d}{:02d}".format(Y,XX))

