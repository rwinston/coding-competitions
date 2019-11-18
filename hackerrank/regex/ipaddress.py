# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

for _ in range(int(input())):
    s = input()
    m = re.match('^(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}(([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]))$',s)
    if m:
        print('IPv4')
    elif re.match('^([a-f0-9]+:?){8}$',s):
        print ('IPv6')
    else:
        print('Neither')
