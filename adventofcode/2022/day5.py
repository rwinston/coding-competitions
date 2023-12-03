import os
import numpy as np


def readData() -> list[list]:
    with open('2022/day5.dat', 'r') as f:
        lines = f.read()
    data = lines.split('\n\n')
    blocks = readBlocks(data[0])
    commands = readCommands(data[1])
    return [blocks,commands]

def readBlocks(lines) -> list[list]:
   print(lines)
   stack = lines.split("\n")
   idx=[index for index,char in enumerate(stack[-1]) if char != ' ']
   blocks = np.array_split([s[x] for x in idx for s in stack[:-1] if s != ' '], len(stack))
   return list(map(lambda x:x[x!=' '], blocks))

def readCommands(lines) -> list[list]:
    commands = []
    for line in lines.split('\n'):
        arr = list(map(int, line.split(' ')[1:6:2]))
        commands.append(arr)
    return commands
    
def part1(blocks, commands) -> list[list]:
    for command in commands:
       for i in range(command[0]):
           fromBlock, toBlock = command[1]-1, command[2]-1
           item = blocks[fromBlock][0]
           blocks[fromBlock] = np.delete(blocks[fromBlock], 0)
           blocks[toBlock] = np.insert(blocks[toBlock], 0, item)
    return blocks


def part2(blocks, commands) -> list[list]:
    for command in commands:
       stack = []
       fromBlock, toBlock = command[1]-1, command[2]-1
       for i in range(command[0]):
            stack.append(blocks[fromBlock][i])
        
       blocks[fromBlock] = np.delete(blocks[fromBlock],list(range(len(stack))))
       blocks[toBlock] = np.insert(blocks[toBlock], 0, stack)
    return blocks


blocks, commands = readData()
p1 = list(map(lambda x: x[0], part1(blocks, commands)))

blocks, commands = readData()
p2 = list(map(lambda x: x[0], part2(blocks, commands)))
