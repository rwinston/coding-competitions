import re

tags = {}
for _ in range(int(input())):
    patt=r'<(?<!\/)(\w+)(.*?)>'
    m=re.findall(patt, input())
    for elem in m:
        tag = elem[0]
        if tag not in tags:
            tags[tag] = []
        m2=re.findall('(\w+)=[^ ]+', elem[1])
        for attr in m2:
            if not attr in tags[tag]:
                tags[tag].append(attr)

for t in sorted(tags):
    print('{}:{}'.format(t, (','.join([str(x) for x in sorted(tags[t]) if x!='']) )))
