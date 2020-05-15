"""
Daily Coding Problem #29

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single 
count and character. For example, the string "AAAABBBCCDAA" would be encoded 
as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be 
encoded have no digits and consists solely of alphabetic characters. You can 
assume the string to be decoded is valid.

"""
def encode(string):
    digits = set(range(10))
    unique = set(string)
    assert digits.intersection(unique) == set(),"string to be encoded has digits present"
    stack = []
    u = 0
    encoded_str = ''
    while (u < len(string)):
        if stack == []:
            stack.append(string[u])
        v = u + 1
        while (string[v] == stack[-1]):
            stack.append(string[v])
            v += 1
            if v == len(string):
                break
        encoded_str += "{}{}".format(len(stack),stack[-1])
        stack.clear()
        alpha = v - u
        u += alpha
    return encoded_str


def decode(string):
    list1 = string[1::2]
    list2 = string[::2]
    decoded_str = ''
    for x in range(len(list1)):
        decoded_str += list1[x] * int(list2[x])
    return decoded_str

if __name__ == '__main__':
    string = 'AAAABBBCCDAA'
    encoded_str = encode(string)
    decoded_str = decode(encoded_str)
    print (encoded_str)
    print (decoded_str)