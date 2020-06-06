"""
Implement a group_by_owners function that:
    1. Accepts a dictionary containing the file owner name for each file name.
    2. Returns a dictionary containing a list of file names for each owner name, in any order.
    
For example, for dictionary {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
the group_by_owners function should return {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

"""
import collections
def group_by_owners(input_dict):
    output_dict = collections.defaultdict(list)
    for k,v in input_dict.items():
        output_dict[v].append(k)
    return dict(output_dict)

if __name__ == '__main__':
    x = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}
    print (group_by_owners(x))