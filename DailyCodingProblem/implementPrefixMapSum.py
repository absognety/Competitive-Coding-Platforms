"""
Daily Coding Problem #232

This problem was asked by Google.

Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the 
key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a 
given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5

"""

class PrefixMapSum(object):
    
    def __init__(self):
        self.map = dict()
        
    def insert(self,key:str,value:int) -> None:
        self.map[key] = value
        
    def total(self,prefix:str) -> int:
        sums = 0
        if self.map:
            for k in self.map:
                if k.startswith(prefix):
                    sums += self.map[k]
        return sums
    
if __name__ == '__main__':
    mapsum = PrefixMapSum()
    mapsum.insert("columnar",3)
    assert mapsum.total("col") == 3, "Not matched"
    mapsum.insert("column", 2)
    assert mapsum.total("col") == 5, "Not matched"
                