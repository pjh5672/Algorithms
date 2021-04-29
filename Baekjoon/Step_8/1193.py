x = int(input())
cnt = 0
i = 0

while x > cnt:
    i += 1
    cnt += i

start_i = cnt - i
find_i = x - start_i

if i % 2 == 0:
    for j in range(1,i+1):
        if j == find_i:
            print(f"{j}/{i+1-j}")
else:
    for j in range(1,i+1):
        if j == find_i:
            print(f"{i+1-j}/{j}")