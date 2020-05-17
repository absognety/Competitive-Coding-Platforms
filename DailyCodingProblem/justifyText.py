"""

Daily Coding Problem #28

This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer 
line length k, return a list of strings which represents each line, fully 
justified.

More specifically, you should have as many words as possible in each line. 
There should be at least one space between each word. Pad extra spaces when 
necessary so that each line has exactly length k. Spaces should be distributed 
as equally as possible, with the extra spaces, if any, distributed starting 
from the left.

If you can only fit one word on a line, then you should pad the right-hand 
side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words 
["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, 
you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

Solution:
    Inspired from this source: https://fthiella.github.io/justify-text/

"""

#The logic is going to be like this:
#
#I keep a buffer that holds all words that can fit into a single line. 
#This buffer is empty at first.
#
#From the given array I read each word, one by one. I eventually split each 
#word into k-sized chunks.
#
#Is the current word / word chunk going to fit into the current line? If 
#there’s still space for it I am going to add it to the current line buffer.
#
#If the current word / chunk won’t fit, I am going to output the current 
#line (all words in the buffer, with proper space justification). 
#The buffer will then be set to contain only the current word.
#
#When I am finished reading all words, I am going to output the current 
#line (unless the buffer is empty, which will happen only if the array of 
#      words is empty as well)

def justify(words,k):
    res = []
    current_length = 0
    current_words = []
    for word in words:
        #take every element from given list
        for s in range(0,len(word),k):
            # split each word into k-sized tokens
            token = word[s:s+k]
            # try to add a new word to current_words / current_length
            if len(token) + current_length + len(current_words) <= k:
                #can fit into a line
                current_words.append(token)
                current_length += len(token)
            else:
                #can't fit into a line
                res.append(justify_line(current_words, current_length, k))
                current_words = [token]
                current_length = len(token)
                
    if current_words:
        res.append(justify_line(current_words, current_length, k))
        
    return res


def justify_line(w,l,k):
    if len(w) == 0:
        return w[0].ljust(k)
    else:
        narrow_spaces, wider_words = divmod(k - l, len(w)-1)
        ns = " " * narrow_spaces
        ws = " " * (narrow_spaces + 1)
        return ns.join([ws.join(w[0:wider_words+1]), *w[wider_words+1:]])
    
#If the current line contains only one word then I’ll just return this word 
#left-justified with spaces at the right (as from the problem specs).
#
#If instead the line is composed by more words, we have to calculate:
#
#the total number of spaces needed (k - l)
#
#the minimum number of spaces between each word (total numer of spaces DIV 
#number of words minus one)
#
#the number of words that require an additional space (total number of spaces 
#MOD number of words minus one)
       
if __name__ == '__main__':
    words = ["the", "quick", "brown", "fox",
		"jumps", "over", "the", "lazy", "dog"]
    k = 16
    print("\n".join(justify(words, k)))