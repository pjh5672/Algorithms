L = []
N = 9

for _ in range(N):
    i = int(input())
    L.append(i)

print(max(L))
print(L.index(max(L))+1)