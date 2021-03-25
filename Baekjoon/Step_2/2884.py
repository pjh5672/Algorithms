A, B = input().split(' ')
A, B = int(A), int(B)

if B < 45:
    B = B + 60 - 45
    A -= 1
    if A < 0:
        A = 23
else:
    B -= 45

print(f'{A} {B}')
