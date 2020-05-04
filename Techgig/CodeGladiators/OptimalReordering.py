"""
Tyson is all prepared for the Beyblade World Championship. 
The tournament is team-based and each team can have N 
members. A player can fight against a single player only. Team G-Revolution 
is all excited and pumped up as they have practised a 
lot. Kenny, the mind of team G-Revolution, has created a 
database where he has the data about the power of other 
teams’ members and his own team members. The tournament 
is going to start in some time and Kenny moves to the cafeteria to have a 
snack before the competition.

The team G-Revolution is to fight in some time and they are tensed up as someone has kidnapped 
Kenny from the cafeteria. They have made a police complaint and the police are searching for 
Kenny. Luckily, they have found his device with all the data. The problem is, the data is present 
randomly and not in the order they have to fight the opponent. Team G-Revolution wants to win at 
any cost and for that, they need the order in which they have to fight optimally to win the 
maximum number of battles.



A player can win only when his/her beyblade power is strictly greater than the opponents beyblade 
power.



Example:

Consider the team size is 3, N = 3


The 3 players of both the teams are shown with their beyblade powers.

Team G-Revolution is presented in the order: Tyson(20), Max(30), Ray(50)

Team All Starz is presented in the order: Michael(60), Eddy(40), Steve(25)



With the given arrangement, Team G-Revolution would be able to win only 1 fight. Team G-Revolution 
should be shuffled in an optimal manner as below:
    
The maximum number of fights Team G-Revolution can win is 2 when they are arranged optimally or 
fight in an optimal order.



Team G-Revolution needs help with the device. Tyson has heard about your skills and called you 
up to help them shuffle their positions in an order such that they would be able to win the 
maximum number of fights. Can you help Tyson and Team G-Revolution?



Input Format
The first line of input consists of the number of test cases, T

The first line of each test case consists of the number of members each team can have, N.

The second line of each test case consists of N space-separated integers representing the power 
of beyblades of Team G-Revolution members.


The third line of each test case consists of N space-separated integers representing the power 
of beyblades of opponent team members.

Constraints
1<= T <=100000
1<= N <=100000

0<= Power of Beyblade <= LLONG_MAX 



Output Format
For each test case, print the maximum number of fights Team G-Revolution can win if they go to 
fight in an optimal manner.

Sample TestCase 1
Input
1
10
3 6 7 5 3 5 6 2 9 1 
2 7 0 9 3 6 0 6 2 6 
Output
7
"""

#Greedy approach may not be right/generic solution
def optimalReOrder(g_rev,oppo,N):
    arr1 = g_rev.copy()
    arr2 = oppo.copy()
    i = 0
    j = 0
    k = i
    while ((i < N) and (j < N)):
        if (arr1[k] <= arr2[j]):
            if k == N-1:
                pass
            else:
                k += 1
                continue
        else:
            temp = arr1[i]
            arr1[i] = arr1[k]
            arr1[k] = temp
        i += 1
        j += 1
        k = i
    print (arr1)
    print (arr2)
    

#merge sort approach (There might be a bug here..)    
def optimal_reorder(g_rev,oppo,N):
    tagged_grev = [('d',i) for i in g_rev]
    tagged_oppo = [('a',i) for i in oppo]
    merged = tagged_grev + tagged_oppo
    merged = sorted(merged,key=lambda x: x[1])
    max_wins = 0
    for i in range(len(merged)-1):
        print (i)
        if set((merged[i][0],merged[i+1][0])) == {'a','d'}:
            if (merged[i][0] == 'a') and (merged[i+1][0] == 'd'):
                if (merged[i][1] < merged[i+1][1]):
                    print (merged[i][1],merged[i+1][1])
                    max_wins += 1
    return max_wins
    

if __name__ == '__main__':
    T = int(input())
    for tcs in range(T):
        N = int(input())
        g_rev = list(map(int,input().strip().split()))
        oppo = list(map(int,input().strip().split()))
        optimalReOrder(g_rev,oppo,N)
        print (optimal_reorder(g_rev,oppo,N))