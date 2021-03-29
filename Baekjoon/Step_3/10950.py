T = int(input())
tmp = []

for _ in range(T): 
    A, B = input().split(' ')
    A, B = int(A), int(B)
    tmp += [A + B]

for i in range(T): 
    print(tmp[i])

