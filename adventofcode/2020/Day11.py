from copy import deepcopy

def dump(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end="")
        print()

def occupied(matrix,i,j):
    occupied = 0
    for x,y in [(x,y) for x in (-1,0,1) for y in (-1,0,1)]:
        if (x==0 and y==0): continue
        x = x+i
        y = y+j
        if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and  matrix[x][y]=='#':
            occupied+=1
    return occupied
        
f = open('c:/temp/p11.txt')
matrix = [list(x.rstrip("\n")) for x in f.readlines() if len(x)>0]

def part1(matrix):
    work = deepcopy(matrix)
    while True:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='.':
                    continue
                occ = occupied(matrix,i,j)
                if (matrix[i][j]=='L' and occ == 0):
                    work[i][j] = '#'
                elif (matrix[i][j]=='#' and occ >= 4):
                    work[i][j]='L'

        if (matrix==work):return work
        matrix = deepcopy(work)

def occupied2(matrix,i,j):
    occupied = 0
    for x,y in [(x,y) for x in (-1,0,1) for y in (-1,0,1)]:
        seen = False
        if (x==0 and y==0): continue
        xx = x+i
        yy = y+j
        while 0<=xx<len(matrix) and 0<=yy<len(matrix[0]) and not seen:
            if matrix[xx][yy]=='L':
                seen = True
            if matrix[xx][yy]=='#':
                occupied+=1
                seen = True
            elif matrix[xx][yy]=='.':
                xx+=x
                yy+=y        
        
    return occupied

def part2(matrix):
     work = deepcopy(matrix)
     while True:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='.':
                    continue
                occ = occupied2(matrix,i,j)
                if (matrix[i][j]=='L' and occ == 0):
                    work[i][j] = '#'
                elif (matrix[i][j]=='#' and occ >= 5):
                    work[i][j]='L'
        if (matrix==work):return work
        matrix = deepcopy(work)
        
# Part 1
print(sum(x.count('#') for x in part1(matrix)))

# Part 2
print(sum(x.count('#') for x in part2(matrix)))
