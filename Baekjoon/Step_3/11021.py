import sys

T = int(sys.stdin.readline().rstrip())
tmp = []

for _ in range(T): 
    A, B = sys.stdin.readline().split(' ')
    A, B = int(A), int(B)
    tmp += [A + B]

for i in range(T): 
    print(f'Case #{i+1}: {tmp[i]}')