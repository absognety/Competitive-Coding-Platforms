"""
Daily Coding Problem #439

This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented 
as (origin, destination) pairs, and a starting airport, compute the 
person's itinerary. If no such itinerary exists, return null. If there 
are multiple possible itineraries, return the lexicographically 
smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), 
                                        ('YUL', 'YYZ'), ('HKO', 'ORD')] 
and starting airport 'YUL', you should return the list 
['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] 
and starting airport 'COM', you should return null.

Given the list of flights 
[('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting 
airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] 
even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. 
However, the first one is lexicographically smaller.

"""

from typing import List,Tuple
def getItinerary(flights:List[Tuple[str,str]],
                 starting_airport:str) -> List[str]:
    count_flights = len(flights)
    cFailure = 0
    cSuccess = 0
    itinerary = [starting_airport]
    while True:
        for sd in range(len(flights)):
            if flights[sd][0] == starting_airport:
                starting_airport = flights[sd][1]
                itinerary.append(starting_airport)
                flights.remove((flights[sd][0],flights[sd][1]))
                cSuccess += 1
                break
            else:
                if sd == len(flights)-1:
                    cFailure += 1
                    break
        if cSuccess == count_flights:
            break
        elif cSuccess + cFailure == count_flights:
            itinerary = []
            break
        elif cFailure == count_flights:
            itinerary = []
            break
    print (cSuccess,cFailure)
    return itinerary
    

if __name__ == '__main__':
    flights = [('SFO', 'HKO'), ('YYZ', 'SFO'), 
               ('YUL', 'YYZ'), ('HKO', 'ORD')]
    s = 'YUL'
    print (getItinerary(flights, s))
    
    
    flights = [('SFO', 'COM'), ('COM', 'YYZ')]
    s = 'COM'
    print (getItinerary(flights, s))
    
    flights = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]
    s = 'A'
    print (getItinerary(flights, s))