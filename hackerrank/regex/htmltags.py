# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

tags = set()
for _ in range(int(input())):
    m=re.findall(r'<(?!\/)\s*([A-Za-z0-9]+)[^>]*?>', input())
    for t in m:
        tags.add(t)

print(';'.join(map(str, sorted(tags))))    
