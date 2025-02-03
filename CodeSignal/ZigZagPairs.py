"""

Problem Statement:

Let's say a triple (a, b, c) is a zigzag if either a < b > c or a > b < c.

Given an array of integers numbers, your task is to check all the triples of its consecutive elements for being a zigzag. 
More formally, your task is to construct an array of length numbers.length - 2, where the ith element of the output array 
equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, and 0 otherwise.

Example

For numbers = [1, 2, 1, 3, 4], the output should be solution(numbers) = [1, 1, 0].

(numbers[0], numbers[1], numbers[2]) = (1, 2, 1) is a zigzag, because 1 < 2 > 1;
(numbers[1], numbers[2] , numbers[3]) = (2, 1, 3) is a zigzag, because 2 > 1 < 3;
(numbers[2], numbers[3] , numbers[4]) = (1, 3, 4) is not a zigzag, because 1 < 3 < 4;
For numbers = [1, 2, 3, 4], the output should be solution(numbers) = [0, 0];

Since all the elements of numbers are increasing, there are no zigzags.

For numbers = [1000000000, 1000000000, 1000000000], the output should be solution(numbers) = [0].

Since all the elements of numbers are the same, there are no zigzags.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] array.integer numbers

An array of integers.

Guaranteed constraints:
3 ≤ numbers.length ≤ 100,
1 ≤ numbers[i] ≤ 109.

[output] array.integer

Return an array, where the ith element equals 1 if the triple (numbers[i], numbers[i + 1], numbers[i + 2]) is a zigzag, 
and 0 otherwise.
"""

## Solution
def solution(numbers):
    size_of_numbers = len(numbers)
    if len(set(numbers)) == 1:
        return [0]
    indicators = []
    for index in range(size_of_numbers-1):
        if numbers[index+1] > numbers[index]:
            indicators.append(True)
        else:
            indicators.append(False)
    if len(set(indicators)) == 1:
        if True in indicators:
            if size_of_numbers % 2 == 0:
                return [0] * (size_of_numbers // 2)
            elif size_of_numbers % 2 == 1:
                return [0] * ((size_of_numbers // 2) + 1)
    output = []
    for index in range(size_of_numbers-2):
        if (numbers[index] < numbers[index+1]) & (numbers[index+1] > numbers[index+2]):
            output.append(1)
        elif (numbers[index] > numbers[index+1]) & (numbers[index+1] < numbers[index+2]):
            output.append(1)
        else:
            output.append(0)
    return output
