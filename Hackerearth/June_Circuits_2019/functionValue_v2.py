import sys
 
T, mod = map(int, sys.stdin.readline().split())
 
# I multiply mod by 4 because I cannot use modular inverse
mod = mod * 4
 
 
def func(n):
    
    # Compute the value of f(n)
    # The general formula is:
    # f(n) = 2 * ( sum( (-1)^i*(-1)^(n//2)* 3^i), i = 1 to n//2 - 1) + 1  
    #
    # For example if we have to compute f(8) then we have:
    # f(8) = 2*3^3 - 2*3^2 + 2*3 + 1
    
    # All values have multiplied by 4
    if n <= 2:
        return 4
    
    if n % 2 == 1:
        return ( 4 * pow(3, n//2, mod) ) % mod
    else:
        if (n // 2 ) % 2 == 0:
            return ( 6 * ( pow(3, n//2 - 1, mod) + 1 ) + 4 ) % mod
        else:
            return ( 6 * ( pow(3, n//2 - 1, mod) - 1 ) + 4 ) % mod
 
 
for _ in range(T):
    L, R = map(int, sys.stdin.readline().split())  
    
    # Compute the sum of odd elements 
    # (e.g for (L, R) = (5, 20) we have f(5) + f(7) + f(9) + ... + f(19)
    #
    # If n is odd we have: f(n) = 3^(n//2)
    # For the above example sum = 3^2 + 3^3 + ... + 3^9
 
    # Find first power of 3 
    f_elem = L // 2
    
    # Find last power of 3
    l_elem = (R - 1) // 2
    
    # Finally we have total = 3^f_elem + 3^(f_elem+1) + ... + 3^(l_elem)
    #
    # The general formula is sum = 1/2 * ( 3^(l_elem+1) - 3^(f_elem) ) and 
    # because we multiply all by 4 we have
    # sum = 2 * ( 3^(l_elem+1) - 3^(f_elem) )    
    total = ( ( pow(3, l_elem+1, mod) - pow(3, f_elem, mod) ) * 2 ) % mod
 
    # Compute the sum of even elements
    # (e.g for (L, R) = (5, 20) we have f(6) + f(8) + f(10) + ... + f(20)
    
    # Find first element that is an even number
    if L % 2 == 0:
        f_even = L
    else:
        f_even = L + 1
    
    # Find last element that is an even number
    if R % 2 == 0:
        l_even = R
    else:
        l_even = R - 1
    
    # Count the number of even elements
    evens = (R - f_even) // 2 + 1
 
    # Let's take an example:
    # f(8) = 2*f(7) - f(6) + 2 ==> f(6) + f(8) = 2*f(7) + 2
    
    # So in our example the sum of even elements is:
    # f(6) + f(8) + f(10) + f(12) + f(14) + f(16) + f(18) + f(20) =
    # = 2*f(7) + 2 + 2*f(11) + 2 + 2*f(15) + 2 + 2*f(19) + 2
    
    if evens % 2 == 0:
    
        # if the number of even elements is even we have the formula
        # a) all powers of 3 are odd numbers. total = 2 * sum( 3^(2*i + 1) ) + 2 * evens and finally
        # b) all powers of 3 are even numbers. total = 2 * sum( 3^(2*i) ) + evens and finally
        #
        # and the general formulas for sums are:
        # a) sum = 3/4 * ( 9^(n+1) - 9^k)
        # b) sum = 1/4 * ( 9^(n+1) - 9^k)
        # where n, k is first and last i in the above formulas
        
        f_even += 2
        
        # Find first and last power of i
        k = (f_even // 2 - 1) // 2 
        n = (l_even // 2 - 1) // 2
        
        # Compute the sum of even elements
        # All formulas have multiplied by 4
        if f_even % 4 != 0:
            total = ( total + ( ( pow(9, n+1, mod) - pow(9, k, mod)) ) % mod ) % mod
        else:
            total = ( total + ( 3 * ( pow(9, n+1, mod) - pow(9, k, mod)) ) % mod ) % mod
    
        # Add the evens multiplied by 4 
        total = ( total + 4 * evens ) % mod
 
    else:
        
        # In the case that we have odd number of even elements we have to compute the value 
        # of the first even element and after that we follow the above procedure
        
        # Compute the value of first even element
        total = ( total + func(f_even) ) % mod
        
        # Compute the value of all the other even elemnts
        # with the above procedure
        f_even += 4
        
        k = ( f_even // 2 - 1 ) // 2 
        n = ( l_even // 2 - 1 ) // 2
        
        if f_even % 4 != 0:
            total = ( total + ( ( pow(9, n+1, mod) - pow(9, k, mod)) ) % mod ) % mod
        else:
            total = ( total + ( 3 * ( pow(9, n+1, mod) - pow(9, k, mod)) ) % mod ) % mod
        
        # We have to remove first even element
        total = ( total + 4 * ( evens // 2 ) * 2 ) % mod
        
    
    # we finally divide by 4
    print(total // 4)
    
