"""
Daily Coding Problem #152

This problem was asked by Triplebyte.

You are given n numbers as well as n probabilities that sum up 
to 1. Write a function to generate one of the numbers with its 
corresponding probability.

For example, given the numbers [1, 2, 3, 4] and probabilities 
[0.1, 0.5, 0.2, 0.2], your function should return 1 10% of the 
time, 2 50% of the time, and 3 and 4 20% of the time.

You can generate random numbers between 0 and 1 uniformly.

"""

import random
def generate_numbers(numbers,probs):
    n = len(numbers)
    #generate a random number between 0 and 1
    r = random.uniform(0, 1)
    total = probs[0]
    for i in range(1,n+1):
        if r <= total:
            return (numbers[i-1])
        total += probs[i]
    return ("non-zero exit status")

#Test the function
numbers = [1,2,3,4]
probs = [0.1,0.5,0.2,0.2]
print (generate_numbers(numbers, probs))