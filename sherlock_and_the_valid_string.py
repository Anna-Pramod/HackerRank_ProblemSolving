#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
def isValid(s):
    a = Counter(s)
    v=list(a.values())
    c=Counter(v)
    k=list(c.keys())
    if(len(s)==1 or (max(k)-min(k)==0)):
        return ("YES")
    elif (len(k)<=2) and max(k)-min(k)==1 and c.get(max(k))==1:
        return ("YES")
    elif (len(k)<=2) and min(k)==1 and c.get(min(k))==1:
        return ("YES")
    else:
        return ("NO")
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
