import sys

N, X = sys.stdin.readline().split(' ')
N, X = int(N), int(X)

C = sys.stdin.readline().split(' ')
C = C[:N]

for i in range(N):
    if int(C[i]) < X:
        print(int(C[i]), end=' ')