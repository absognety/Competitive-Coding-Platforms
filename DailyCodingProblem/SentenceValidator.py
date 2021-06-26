"""
Daily Coding Problem #431

This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters 
and determines whether they form valid sentences. If a sentence is 
valid, the program should print it out.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase 
letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or 
terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following 
a word.

"""
import re
def validateSentence(sentence:str) -> None:
    terminal_marks = [".","?","!","$"]
    try:
        assert sentence[0].isupper() == True, "Sentence doesn't start with capital letter"
        assert sentence == sentence.capitalize(), "Rest of characters except first letter are not lowercase"
        words = sentence.split(" ")
        if "" in words:
            raise AssertionError("Single space between words condition failed")
        assert (sentence[-1] in terminal_marks), "sentence is not ending with terminal mark"
        other_characters = sentence[1:-1]
        search = re.compile(r'[^a-z,;:\s]').search
        checker = not bool(search(other_characters))
        assert checker == True, "All other characters are not lowercase or belong to separators"
        print ("All validations are passed")
        print (sentence)
    except Exception as e:
        print (str(e))
        
    
if __name__ == '__main__':
    s = "Abraham is the best president, of U.S.A."
    validateSentence(s)
    s1 = "Abraham is the best president, of u.s.a."
    validateSentence(s1)
    s2 = "Abraham is the best president, of usa."
    validateSentence(s2)