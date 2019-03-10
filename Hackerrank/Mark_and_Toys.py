#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices_len = len(prices)
    suitable = []
    for l in range(1,prices_len+1):
        for combination in itertools.combinations(prices,l):
            if sum(combination) <= k:
                suitable.append(len(combination))
    return (max(suitable))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
