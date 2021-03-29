import sys

T = int(sys.stdin.readline().rstrip())
As = []
Bs = []

for _ in range(T): 
    A, B = sys.stdin.readline().split(' ')
    As.append(int(A))
    Bs.append(int(B))

for i in range(T): 
    print(f'Case #{i+1}: {As[i]} + {Bs[i]} = {As[i]+Bs[i]}')