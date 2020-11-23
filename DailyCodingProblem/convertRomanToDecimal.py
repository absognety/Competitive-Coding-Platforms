"""

Daily Coding Problem #216

This problem was asked by Facebook.

Given a number in Roman numeral format, convert it to decimal.

The values of Roman numerals are as follows:

{
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
In addition, note that the Roman numeral system uses subtractive 
notation for numbers such as IV and XL.

For the input XIV, for instance, you should return 14.


"""

home = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}

def roman2decimal(numeral):
    symbols = list(numeral)
    total = 0
    for i in range(len(symbols)-1):
        if home[symbols[i]] >= home[symbols[i+1]]:
            total += home[symbols[i]]
        else:
            total += (home[symbols[i+1]] - home[symbols[i]])
    return total

print (roman2decimal("XIV"))
print (roman2decimal("IV"))
print (roman2decimal("XL"))
print (roman2decimal("XXIV"))