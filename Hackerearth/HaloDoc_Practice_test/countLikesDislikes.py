'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

def count_likes_dislikes(str1,str2):
    C = 0
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            C += 1
    return C


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print (count_likes_dislikes(str1,str2))