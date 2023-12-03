import re
from collections import defaultdict
from functools import reduce 

def checkLimit(game):
    limits = {'red':12, 'green':13, 'blue':14}

    for cube in game.split(","):
        cubeCount, cubeName = cube.strip().split(" ")
        if int(cubeCount) > limits[cubeName]:
            return False
    return True
            

def part1(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    possibleGames = set()
    for line in lines:
        id = line.split(":")[0].split(" ")[1]
        games = line.split(":")[1].split(";")
        possibleGames.add(id)
        for game in games:
            if (checkLimit(game) == False):
                possibleGames.remove(id)
                break     
    return(sum([*map(int, possibleGames)]))

def part2(filename):
    lines = []
    products = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    possibleGames = set()
    for line in lines:
        id = line.split(":")[0].split(" ")[1]
        games = line.split(":")[1].split(";")
        cubeCounts = defaultdict(list)
        for game in games:
            for cube in game.split(","):
               cubeCount, cubeName = cube.strip().split(" ")
               cubeCounts[cubeName].append(int(cubeCount)) 
        products.append(reduce(lambda x,y:x*y, [*map(lambda x:max(x[1]), cubeCounts.items())]))
    return sum(products)


print(part2('2023/day2.dat'))