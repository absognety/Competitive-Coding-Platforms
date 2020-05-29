"""
Daily Coding Problem #17

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 
containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a 
file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a 
second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file 
within our file system. For example, in the second example above, the longest absolute 
path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of 
the longest absolute path to a file in the abstracted file system. If there is no file 
in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
"""

def longestAbsolutePath(string):
    """
    write your code here - two scenarios possible:
        1. file (string with period exists)
        2. no file exists (longest absolute path may have to contain only sub-directories)
    """
    lines = string.splitlines()
    files = []
    for line in lines:
        if '.' in line:
            files.append((line,line.count("\t")))
    files = sorted(files,key=lambda x: x[1],reverse=True)
    last_file = files[0][0]
    last_index = lines.index(last_file)
    t = last_file.count("\t")
    result = []
    while (t >= 1):
        assert last_file.count("\t")==t,"number of tabs are correctly present"
        tokens = last_file.split("\t")
        result.append(tokens[-1])
        last_index -= 1
        last_file = lines[last_index]
        t -= 1
    result.append("dir")
    result = "/".join(result[::-1])
    return len(result),result
    
if __name__ == '__main__':
    s1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
    s2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print (longestAbsolutePath(s1))
    print (longestAbsolutePath(s2))