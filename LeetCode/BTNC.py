# Solution using Dynamic Programming

def highestPossibleScore(scores:int,ages:int) -> int:
    n = len(ages)
    ageScorePair = list(zip(scores,ages))
    ageScorePair = sorted(ageScorePair,key=lambda x:(x[0],x[1]))
    dp = [None] * n
    max_score = 0
    for i in range(0,n):
        dp[i] = search(dp,ageScorePair,i) + ageScorePair[i][0]
        max_score = max(max_score,dp[i])
    return max_score


def search(dp, ageScorePair, i):
    _max_ = 0
    for j in range(0,i):
        if (dp[j] > _max_) & (ageScorePair[j][1]<=ageScorePair[i][1]):
            _max_ = dp[j]
    return _max_

if __name__ == '__main__':
    scores = [1,3,5,10,15]
    ages = [1,2,3,4,5]
    print (highestPossibleScore(scores=scores,
                                ages=ages))
    
    scores = [4,5,6,5]
    ages = [2,1,2,1]
    print (highestPossibleScore(scores=scores,
                                ages=ages))
    
    scores = [1,2,3,5] 
    ages = [8,9,10,1] 
    print (highestPossibleScore(scores=scores,
                                ages=ages))
    

    scores = [1,1,1,1,1,1,1,1,1,1]
    ages = [811,364,124,873,790,656,581,446,885,134]
    print (highestPossibleScore(scores=scores,
                                ages=ages))
    
    scores = [1,3,7,3,2,4,10,7,5]
    ages = [4,5,2,1,1,2,4,1,4]
    print (highestPossibleScore(scores=scores,
                                ages=ages))
