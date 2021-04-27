word = str(input())
characters = list(range(ord('a'), ord('z')+1))

for x in characters:
    print(word.find(chr(x)))
