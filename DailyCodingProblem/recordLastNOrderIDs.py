"""
Daily Coding Problem #16
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:
    1. record(order_id): adds the order_id to the log
    2. get_last(i): gets the ith last element from the log. i is guaranteed to be smaller 
    than or equal to N.
    3. You should be as efficient with time and space as possible.
    

Approach: Stack data structure seems like a good fit, let's try..

"""

def record(order_id):
    stack.append(order_id)
    return

def get_last(i):
    assert i <= N,"i is not less than or equal to N"
    ele = stack.pop(-1 * i)
    stack.insert(N - i,ele)
    return ele

if __name__ == '__main__':
    N = int(input())
    stack = []
    for n in range(N):
        order_id = input()
        record(order_id)
    while True:
        print ("\n Please enter break to get out of loop")
        index = input()
        if index == 'break':
            break
        try:
            index = int(index)
        except:
            raise Exception("The index you entered is not valid")
        print (get_last(index))