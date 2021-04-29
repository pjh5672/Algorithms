A, B, V = list(map(int, input().split()))

d = (V-B)/(A-B)
print(int(d) if d == int(d) else int(d)+1)