"""
Generate a graph from given list of words composed of characters:
    b, f, g, q
    
words:
    bgg
    fbq
    fqf
    ffq,
    gfg

Write methods for this graph as follows:
    class Graph:
        def add(self,c1,c2) => add edge between c1 and c2
        def remove(self,c2,c2) => removes edge between c1 and c2
        def outgoing(self,c) => returns a list of characters
        def incoming(self,c) => returns a list of characters
"""