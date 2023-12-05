def prepare(filename):
    lines = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    winningNumbers = []
    draws = []
    scores = []

    for line in lines:
        parts  = line.strip().split('|')
        winningNumbers.append({*map(lambda x:int(x), parts[0].split(':')[1].split())})
        draws.append({*map(lambda x:int(x), parts[1].split())})
    
    for i,draw in enumerate(draws):
       score = sum([*map(lambda x:x in winningNumbers[i], draw)])
       scores.append(score)
       
    return scores

def part1(filename):
    scores = prepare(filename)
    return sum([*map(lambda x:2**(x-1) if x > 0 else 0, scores)])
    
def part2(filename):
    scores = prepare(filename)
    cards = [1]*len(scores)
    print(scores)

    for i,score in enumerate(scores):
        print('score=',score)
        score = score * cards[i]
        for j in range(i+1,(i+score)):
            print('j=',j)
            cards[j] += 1
        
        print('Won',score,'copies of ',*range(i+1,i+score+1))
        
    return(cards)


print(part1('2023/day4.dat'))
print(part2('2023/day4_test1.dat'))
