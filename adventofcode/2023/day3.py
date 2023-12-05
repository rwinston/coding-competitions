def isSymbol(x):
    return (x.isdigit() == False and x != '.')     

def isGear(x):
    return (x=='*')            


def prepare(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    matrix = []
    matrix.append([* '.' * len(lines[0]) + '.'])
    for i,line in enumerate(lines):
        matrix.append([* '.' + line.strip() + '.'])
    matrix.append([* '.' * len(lines[0]) + '.'])
    return(matrix)

numberCoords = []
gearLocations = []
coordsToNumber = {}

def part1(filename):
    matrix = prepare(filename)
    validNums = []
    cols = len(matrix[0])
    for i,row in enumerate(matrix):
        num = ''
        thisNumValid = False
        for j in range(cols):
            if(row[j].isdigit()):
                num += row[j]
                if (isSymbol(row[j-1]) 
                    or isSymbol(row[j+1]) 
                    or isSymbol(matrix[i-1][j-1])
                    or isSymbol(matrix[i-1][j])
                    or isSymbol(matrix[i-1][j+1])
                    or isSymbol(matrix[i+1][j-1])
                    or isSymbol(matrix[i+1][j])
                    or isSymbol(matrix[i+1][j+1])
                    ):
                    thisNumValid = True
            else:
                if (thisNumValid == True and len(num)>0):
                    validNums.append(int(num))
                    numberCoords.append((i,j-len(num)))
                    coordsToNumber[(i,j-len(num))] = num
                num = ''
                thisNumValid = False
    return sum(validNums)
    

def part2(filename):
    gearRatio = 0
    matrix = prepare(filename)
    for i,row in enumerate(matrix):
        for j,cell in enumerate(row):
            if (isGear(cell)):
                gearLocations.append((i,j))
    
    print(gearLocations)
    
    for gearLocation in gearLocations:
        print('Checking',gearLocation,'for nums',numberCoords)
        
        numsWithinLocation = []
        gridX = {gearLocation[0]-1, gearLocation[0], gearLocation[0]+1}
        gridY = {gearLocation[1]-1, gearLocation[1], gearLocation[1]+1}      
        grid = gridX.union(gridY)
       
        for numCoord in numberCoords:
            number = coordsToNumber[numCoord]
            possibleCoords = {(numCoord[0]+x,numCoord[1]) for x in range(len(number))}
            print('Checking number',number,'at coordinate',numCoord,'=>', possibleCoords, 'in grid',grid)

            if any([*map(lambda x:x in grid, possibleCoords)]):
                print('number ',number,'found in grid',grid)
                numsWithinLocation.append(number)
                next
        
        if (len(numsWithinLocation)==2):
            print('gearLocation at',gearLocation,' has nums',numsWithinLocation)
            gearRatio += numsWithinLocation[0] * numsWithinLocation[1]
    return(gearRatio)

print(part1('2023/day3_test2.dat'))
print(part2('2023/day3_test2.dat'))
