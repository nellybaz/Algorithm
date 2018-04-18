followers = [(3,1), (3, 2)] 
followersLikedTweets = [(1, 23), (2,23), (1,22), (2,22)] 
maximum = 2
ID = 3
def getRecommendedTweets(followGraph_edges, likeGraph_edges, targetUser, minLikeThreshold):
    count = 1
    tweetCount = {}
    if not isinstance(minLikeThreshold, int) or minLikeThreshold < 0 or not likeGraph_edges or not isinstance(likeGraph_edges, list) or not isinstance(followGraph_edges, list) or not followGraph_edges or [item for item in likeGraph_edges if not isinstance(item, tuple)] or [item for item in followGraph_edges if not isinstance(item, tuple)]:
        return []
    else:
        
        targetUser_follows = []
        for user in followGraph_edges:
            #print(user[1])
            if [item for item in followGraph_edges if targetUser in item]:
                targetUser_follows.append(user[1])
                
        for tweet in likeGraph_edges:
            
            if [item for item in likeGraph_edges if item[0] in targetUser_follows]:
                
                if tweet[1] in tweetCount:
                    
                        
                    count = count+1
                    tweetCount[tweet[1]] = count
                else:
                    count = 1
                    tweetCount[tweet[1]] = count
                    
        recommended_tweets = []
        for key in tweetCount:
            if tweetCount[key] >= minLikeThreshold:
                recommended_tweets.append(key)
        
               
    #print(targetUser_follows)
    #print(tweetCount)
    #print(recommended_tweets)
                
            
    return sorted(recommended_tweets)
     
            
            
        
            
    
        
        
print(getRecommendedTweets(followers,followersLikedTweets,ID, maximum))