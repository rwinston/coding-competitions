import re
lines = []
words = []
counts = {}
for _ in range(int(input())):
    lines.append(input())

for _ in range(int(input())):
    word = input()
    words.append(word)
    counts[word]=0

for line in lines:
    for word in words:
        patt = r'\b{}\b'.format(word)
        m=re.findall(patt,line)
        counts[word]+=len(m)

for count in counts:
    print(counts[count])

