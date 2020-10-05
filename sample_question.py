"""
Implement a group_by_owners function that:
    1. Accepts a dictionary containing the file owner name for each file name.
    2. Returns a dictionary containing a list of file names for each owner name, in any order.
    
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

"""
'''
edited by Shouvik Dutta
reason-suppose, we ask to answer if a particular user is able to handle a particular file.
        Then we have to iterarte over the return dict.
        i.e. if 'Output.txt' in  my_dict[i].....tc=>O(n)
        otherwise if we use set, tc=>O(1)
        if counted needed,
                      then make defaultdict(int)
'''
import collections
def group_by_owners(input_dict):
    #output_dict = collections.defaultdict(list)
    my_dict=collections.defaultdict(set)
    for k,v in input_dict.items():
        #output_dict[v].append(k)
        my_dict[v].add(k)
    return dict(my_dict)

if __name__ == '__main__':
    x = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    print (group_by_owners(x))
