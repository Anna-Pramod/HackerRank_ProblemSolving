#!/bin/python3

import math
import os
import random
import re
import sys
def jumpingOnClouds(c):
    ct=0
    i=0
    while i<len(c)-1:
        if i+2<len(c) and c[i+2]==0:
            i+=2
            ct+=1
        else:
            i+=1
            ct+=1
    return ct

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
