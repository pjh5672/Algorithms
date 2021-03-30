import time
import copy

A = input()
new_A = copy.deepcopy(A)

if int(A) < 10:
    A = '0' + A
    new_A = copy.deepcopy(A)
cnt = 0

while True:
    last_num = str(int(new_A[0]) + int(new_A[1]))
    if int(last_num) > 9:
        last_num = last_num[-1]
    new_A = new_A[1] + last_num
    cnt += 1
    if new_A == A:
        break

print(cnt)
