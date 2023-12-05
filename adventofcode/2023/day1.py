import re

def part1(filename):
    lines = []
    with open(filename,'r') as f:
        lines = f.readlines()
    print(lines)
    sum = 0
    for line in lines:
        r = re.findall('[0-9]', line)
        sum += [int(r[0]+r[0]) if len(r)==1 else int(r[0]+r[-1:][0])][0]
    return(sum)    

def part2(filename):
    lines = []
    with open(filename,'r') as f:
        lines = f.readlines()
    PATTERNS = ['one','two','three','four','five','six','seven','eight','nine']
    matchPattern = '(?=(' + '|'.join(PATTERNS) + '|\\d))'
    sum = 0
    def mapNum(x):
        print(x)
        if x in PATTERNS:
            return str(PATTERNS.index(x)+1)
        return x
        
    for line in lines:
        r = [*map(mapNum, re.findall(matchPattern, line))]
        print('line=',line,'r=',r)
        sum+=int(r[0]+r[-1])

    print(sum)




print(part2('2023/day1.dat')) 
