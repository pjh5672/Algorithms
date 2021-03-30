res = 1
N = 3

for _ in range(N):
    i = int(input())
    res *= i

for i in range(10):
    print(str(res).count(str(i)))


