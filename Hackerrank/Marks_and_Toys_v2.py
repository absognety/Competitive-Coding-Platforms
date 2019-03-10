#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the maximumToys function below.
def maximumToys(prices, k):
    total = 0
    count = 0
    prices = sorted(prices)
    for p in prices:
        total += p
        if total <= k:
            count += 1
    return (count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
