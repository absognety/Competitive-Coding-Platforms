"""
Given two strings:
    
    string1 = "abcde"
    string2 = "cdeab"
    
write a function that returns True if string2 can be obtained by rotating
string1 if not return False (rotation can be done by any number of elements)

"""
def rotate(array,m):
    cutoff_arr = array[0:m]
    rotated_arr = array[m:] + cutoff_arr
    return (rotated_arr)

def check_rotation(str1,str2):
    if len(str1) != len(str2):
        return False
    for i in range(1,len(str1)):
        if rotate(str1,i) == string2:
            return True
    return False


def check_rotation2(str1,str2):
    if len(str1) != len(str2):
        return False
    union = str1 * 2
    if str2 in union:
        return True
    return False

if __name__ == '__main__':
    string1 = 'abcde'
    string2 = 'cdeab'
    print (check_rotation(string1,string2))
    print (check_rotation2(string1,string2))
    
    string3 = "abcde"
    string4 = "eabcdf"
    print (check_rotation(string3,string4))
    print (check_rotation2(string3,string4))