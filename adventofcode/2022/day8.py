import os
from itertools import takewhile
from functools import reduce


def readData() -> list[list]:
    matrix = []
    with open('2022/day8.dat', 'r') as f:
        for line in [line.rstrip() for line in f]:
            matrix.append(list(map(int,(list(line)))))
    return matrix

def part1(matrix) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    visible = 2*(rows)+2*(cols)-4  
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            height = matrix[i][j]
            down = [matrix[z][j] for z in range(i+1,rows)]        
            right = [matrix[i][z] for z in range(j+1,cols)]
            left = [matrix[i][z] for z in range(0,j)]
            up = [matrix[z][j] for z in range(0,i)]

            f = lambda y : all(list(map(lambda x:x<height, y)))
            visible += int(any([f(left),f(right), f(up), f(down)]))
           
    return (visible)


def countVisible(l, h):
    count = 0
    for i in l:
        if i < h:
            count +=1 
        else:
            count += 1
            break
    return count

def part2(matrix) -> int:
    rows = len(matrix)
    cols = len(matrix[0])

    maxVisible = 0
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            height = matrix[i][j]
            down = [matrix[z][j] for z in range(i+1,rows)]        
            right = [matrix[i][z] for z in range(j+1,cols)]
            left = [matrix[i][z] for z in range(0,j)]
            up = [matrix[z][j] for z in range(0,i)]

            f = (lambda y: countVisible(y, height))
            counts = list(map(f, [up[::-1], down, left[::-1], right]))
            visible = reduce((lambda x,y: x*y), counts)
            maxVisible = max(visible, maxVisible)
            
    return maxVisible       


print(part1(readData()))
print(part2(readData()))
        

        
