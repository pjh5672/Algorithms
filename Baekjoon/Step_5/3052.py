res = []

for i in range(10):
    inp = int(input())
    res.append(inp%42)
    
res = set(res)
print(len(res))