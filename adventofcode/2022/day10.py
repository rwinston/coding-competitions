import os
from itertools import takewhile
from functools import reduce


def readData() -> list[str]:
    with open('2022/day10test.dat', 'r') as f:
        return [line.rstrip() for line in f]


def readCommands(commands) -> list:
    x = 1
    cycle = 1
    states = []
    for command in commands:
        codes = command.split(' ')
        match codes[0]:
            case 'noop':
                states.append(x)
                cycle+=1
            case 'addx':
                states.append(x)
                states.append(x)
                x += int(codes[1])
                cycle += 2
 
        print('cycle=%i, state=%s' % (cycle, x))
    return states

states =  readCommands(readData())
print(states)
print(len(states))        
cycles = [20, 60, 100, 140, 180, 220]
total = 0
for cycle in cycles:
    print('cycle=%s, state=%s, value=%s, total=%s' % (cycle, states[cycle], cycle*states[cycle],total))
    total += cycle * states[cycle]
    print(total)
print(total) 
