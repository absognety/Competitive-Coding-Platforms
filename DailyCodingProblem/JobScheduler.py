"""
Daily Coding Problem #10
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.

Sol: The solution demonstrated here is simplified version of event scheduling
program

But for more efficient workflow management and monitoring frameworks, please
explore:
    1. Prefect (https://www.prefect.io/)
    2. Airflow (The Apache software foundation)
    3. Crontab (Linux command line tool)
"""
import time
def f(a,b):
    s = a + b
    print ("the sum of 2 numbers {},{} is {}".format(a,b,s))
    d = abs(a-b)
    print ("the absolute difference of 2 numbers {},{} is {}".format(a,b,d))
    product = a*b
    print ("the product of 2 numbers {},{} is {}".format(a,b,product))
    if b != 0:
        div = a/b
        print ("the division answer of 2 numbers {},{} is {}".format(a,b,div))
    else:
        print ("the division of two numbers is not possible")
        
def scheduler(f,m,n):
    f(m,n)

if __name__ == '__main__':
    n = int(input())
    while True:
        time.sleep(n/1000)
        scheduler(f,34,17)
        break