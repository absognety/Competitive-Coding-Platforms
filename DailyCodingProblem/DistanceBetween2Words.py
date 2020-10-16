"""
Daily Coding Problem #153

Find an efficient algorithm to find the smallest distance 
(measured in number of words) between any two given words in a 
string.

For example, given words "hello", and "world" and a text 
content of "dog cat hello cat dog dog hello cat world", 
return 1 because there's only one word "cat" in between the 
two words.

"""

#if given text content is tab-separated words
import itertools
import math
def distance2words(text,w1,w2,sep):
    tokens = text.split(sep)
    w1_loc = []
    w2_loc = []
    for ind,w in enumerate(tokens):
        if w == w1:
            w1_loc.append(ind)
        elif w == w2:
            w2_loc.append(ind)
    paired = itertools.product(w1_loc,w2_loc)
    min_distance = math.inf
    for x,y in paired:
        if abs(y-x-1) < min_distance:
            min_distance = abs(y-x-1)
    return min_distance

#no separatorn but just a raw text
def distance2words_raw(text,w1,w2):
    """
    This is not possible because, distance cannot 
    be expressed in terms of number of words if we cannot 
    identify what the words in the middle are
    
    they can only be identified if there is a separator

    Parameters
    ----------
    text : str
        Text content 
    w1 :  str
        first word
    w2 : str
        second word

    Returns
    -------
    min_distance: int
        minimum distance between 2 words in a text content
    """

text = "dog cat hello cat dog dog hello cat world"
w1,w2 = "hello","world"
print (distance2words(text, w1, w2," "))