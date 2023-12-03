import os
from enum import Enum
import numpy as np

class Mode(Enum):
    DIR = 0
    FILE = 1


class DirNode:
    def __init__(self, name, parent) -> None:
        self.size = 0
        self.name = name
        self.children = []
        self.parent = parent
        self.type = Mode.DIR


root = DirNode('/', None)

def treeSize(node:DirNode, size): 
    if len(node.children)==0:
        return node.name, node.size, node.type
    else:
        node.size += sum([treeSize(child, size)[1] for child in node.children ])  
        return node.name, node.size, node.type     


def part1(node:DirNode, size, stack): 
    if len(node.children)==0:
        stack.append((node.name, node.size, node.type))
        return node.name, node.size, node.type
    else:
        size = sum([part1(child, size, stack)[1] for child in node.children ])  
        stack.append((node.name, node.size, node.type))  
        return node.name, node.size, node.type  

        
def readData() -> list:
    with open('2022/day7.dat', 'r') as f:
        return [line.rstrip() for line in f]    

def buildTree(commands : list[str]) -> DirNode:
    currentNode = root
    for command in commands:
        print('COMMAND: '+command)
        if command.startswith("$"):
            code = command.split(' ')
            match code[1]:
                case 'cd':
                    dirName = code[2]
                    if dirName == '..':
                        thisNode = currentNode.parent
                    elif dirName == '/':
                        thisNode = root
                    else:
                        thisNode = [child for child in currentNode.children if child.name==dirName][0]
                    currentNode = thisNode
        else:
            p1,p2 = command.split(' ')
            if p1 == 'dir':
                currentNode.children.append(DirNode(p2, currentNode))
            else:
                fileNode = DirNode(p2, currentNode)
                fileNode.size = int(p1)
                fileNode.type = Mode.FILE
                currentNode.children.append(fileNode)

buildTree(readData())
print(treeSize(root,0))

stack = []
part1(root, 0, stack)
p1 = sum(list(map(lambda x:x[1], list(filter(lambda x:x[2]==Mode.DIR and x[1]<100000, stack)))))

spaceToDelete = 30000000 - (70000000-root[1]) 
p2 = sorted(list(map(lambda x:x[1], list(filter(lambda x:x[2]==Mode.DIR and x[1]>=spaceToDelete, stack)))))
print(p2[0])