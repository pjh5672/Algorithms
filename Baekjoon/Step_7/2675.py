alphanumeric = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./:"

T = int(input())
assert T < 101

ans = []

for _ in range(T):
    inp = str(input())
    R, S = inp.split(" ")
    assert len(S) > 0
    
    temp = str()
    for x in S:
        temp += x * int(R)
    ans.append(temp)

for i in range(T):
    print(ans[i])