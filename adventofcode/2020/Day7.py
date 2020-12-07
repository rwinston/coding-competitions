import re

f = open('p7')

found = []
def find_paths(start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_paths(node, end, path)
            for newpath in newpaths:
                if len(newpath) > 0:
                    found.append(start)
                    paths.append(newpath)
    return paths


def find(end):
    allpaths = []
    for start in graph.keys():
        allpaths.append(find_paths(start, end))
    return allpaths


graph = {}
counts = {}

for line in f.readlines():
    m = re.search(r'^(\S+ \S+) bags contain', line)
    bag = m.group(1)
    graph[bag] = []
    counts[bag] = []
    for m in re.finditer(r'(\d+) (\S+ \S+) bag(s,)?', line):
        graph[bag].append(m.group(2))
        counts[bag].append((m.group(2), m.group(1)))


def count(bag):
    return 1 + sum(int(n)*count(c) for c, n in counts[bag])


# Part 1
find('shiny gold')
print(len(set(found)))

# Part 2
print(count('shiny gold')-1)



