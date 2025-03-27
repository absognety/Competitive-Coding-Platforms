'''
Bob has an important meeting tomorrow and he has to reach office on time in morning. His general mode of transport is by car 
and on a regular day (no car trouble) the probability that he will reach on time is Pot. 
The probability that he might have car trouble is Pct. 
If the car runs into trouble he will have to take a train and only 2 trains out of the available N trains will get him 
to office on time.

What are the chances that he will reach office on time tomorrow?

Input format

First line: Pct

Second line: Pot

Third line: N

Output format

Probability he will reach in time, rounded to six decimal digits
'''

Pct = float(input().strip())
Pot = float(input().strip())
N = int(input().strip())

# X is the event of reaching office on time
# Y is the event of car working fine.
# P(X) = P(X and Y) + P(X and Y')
# P(X) = P(X/Y) * P(Y) + P(X/Y') * P(Y')

Px = ((1 - Pct) * Pot) + (Pct * 2/N)
print ("%.6f" % (Px))
