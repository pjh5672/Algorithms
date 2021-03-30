import sys

while True:
    A, B = sys.stdin.readline().split(' ')
    A, B = int(A), int(B)

    if A == 0 and B == 0:
        break

    print(A + B)
