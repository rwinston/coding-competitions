import os
from itertools import takewhile
from functools import reduce


def readData() -> list[list]:
    matrix = []
    with open('2022/day8.dat', 'r') as f:
        for line in [line.rstrip() for line in f]:


        
