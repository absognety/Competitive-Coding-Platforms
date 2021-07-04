"""
Daily Coding Problem #219

This problem was asked by Salesforce.

Connect 4 is a game where opponents take turns dropping red or 
black discs into a 7 x 6 vertically suspended grid. The game ends 
either when one player creates a line of four consecutive discs of 
their color (horizontally, vertically, or diagonally), or when 
there are no more spots left in the grid.


Design and implement Connect 4.

"""

def connect4game(m,n):
    grid = [[None for i in range(n)] for j in range(m)]
    while True:
        