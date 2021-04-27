word = input().lower()
chro_words = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in chro_words:
    word = word.replace(i, "c")

print(len(word))