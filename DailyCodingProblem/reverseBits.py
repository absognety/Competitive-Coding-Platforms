"""
Daily Coding Problem #161

This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits 
reversed.

For example, given the binary number 
1111 0000 1111 0000 1111 0000 1111 0000, 
return 0000 1111 0000 1111 0000 1111 0000 1111.

"""

def reverse_bits(binary_string:str) -> str:
    result = []
    for c in binary_string:
        if c != " ":
            if (c == '1') or (c == '0'):
                result.append(str(int(not int(c))))
        elif c == " ":
            result.append(c)
    return "".join(result)

print (reverse_bits("1111 0000 1111 0000 1111 0000 1111 0000"))