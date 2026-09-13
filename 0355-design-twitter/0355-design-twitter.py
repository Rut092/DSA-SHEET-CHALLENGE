from collections import defaultdict
import heapq
class Twitter(object):

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweetMap[userId].append([self.count,tweetId])
        self.count-=1

    def getNewsFeed(self, userID):
        """
        :type userId: int
        :rtype: List[int]
        """
        res = []
        minHeap = []

        self.followMap[userID].add(userID)
        for followeeID in self.followMap[userID]:
            index = len(self.tweetMap[followeeID])-1
            if index>=0:
                count,tweetID = self.tweetMap[followeeID][index]
                heapq.heappush(minHeap,[count,tweetID,followeeID,index-1])

        heapq.heapify(minHeap)
        while(len(res)<10 and minHeap):
            count,tweetId,followeeID,prevIDX = heapq.heappop(minHeap)
            res.append(tweetId)
            if prevIDX>=0:
                count,tweetID = self.tweetMap[followeeID][prevIDX]
                heapq.heappush(minHeap,[count,tweetID,followeeID,prevIDX-1])
        
        return res

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)