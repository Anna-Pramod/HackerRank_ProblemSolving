#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby
def countingValleys(steps, path):
    # Write your code here
    c=0
    v=0
    for i in path:
        if i=="U":
            c+=1
        else:
            c-=1
        if (c==0 and i=="U"):
            v+=1
    return(v)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
