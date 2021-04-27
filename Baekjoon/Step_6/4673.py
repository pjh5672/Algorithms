natural_num = set(range(1, 10001))
generated_num = set()

for i in natural_num:
    for j in str(i):
        i += int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)
for i in self_num:
    print(i)
