"""
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal 
places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.

please refer: https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/
for the theory

"""

import numpy as np
interval = int(input())
circle_points = 0
square_points = 0

i = 0
while (i < (interval ** 2)):
    rand_x = np.random.uniform(-1,1)
    rand_y = np.random.uniform(-1,1)
    d = np.square(rand_x) + np.square(rand_y)
    if d <= 1:
        circle_points += 1
    square_points += 1
    pi = 4 * (np.divide(circle_points,square_points))
    i += 1

#final estimation of final Pi value
print (pi)