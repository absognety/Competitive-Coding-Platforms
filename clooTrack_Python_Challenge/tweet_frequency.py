def tweet_analyzer(TWEETS):
    names=[]
    tweet_ids = []
    for t in TWEETS:
        names.append(t.split()[0])
        tweet_ids.append(t.split()[1])
        
    name_freq={}
    for N in names:
        if N in name_freq:
            name_freq[N]+=1
        else:
            name_freq[N]=1
    distinct_len = len(list(set(list(name_freq.values()))))
    length = len(list(name_freq.values()))
    if (distinct_len==length):
        KEY = [k for k,v in name_freq.items() if v==max(list(name_freq.values()))]
        print (KEY[0],max(list(name_freq.values())))
    else:
        for k in sorted(name_freq):
            print (k,name_freq[k])


if __name__ == '__main__':
    T=int(input())
    for t_c in range(T):
        N_tw = int(input())
        tweets = []
        for n in range(N_tw):
            tweet = input()
            tweets.append(tweet)
        tweet_analyzer(tweets)
