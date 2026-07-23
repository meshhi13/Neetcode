class Twitter:
    def __init__(self):
        self.time = 0
        self.posts = {}
        self.feed = {}
        self.followers = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.posts:
            heapq.heappush(self.posts[userId], (-self.time, tweetId, userId))
        else:
            self.posts[userId] = [(-self.time, tweetId, userId)]
            heapq.heapify(self.posts[userId])

        if userId in self.feed:
            heapq.heappush(self.feed[userId], (-self.time, tweetId, userId))
        else:
            self.feed[userId] = [(-self.time, tweetId, userId)]
            heapq.heapify(self.feed[userId])

        if userId in self.followers:
            for follower in self.followers[userId]:
                if follower in self.feed:
                    heapq.heappush(self.feed[follower], (-self.time, tweetId, userId))
                else:
                    self.feed[follower] = [(-self.time, tweetId, userId)]
                    heapq.heapify(self.feed[follower])

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newC = list(self.feed[userId])
        result = [] 
        k = 0

        while newC and k < 10:
            result.append(heapq.heappop(newC)[1])
            k += 1

        return result
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 

        if followeeId in self.followers:
            if followerId in self.followers[followeeId]:
                return
            self.followers[followeeId].append(followerId)
        else:
            self.followers[followeeId] = [followerId]

        if followeeId in self.posts:
            if followerId in self.feed:
                self.feed[followerId].extend(self.posts[followeeId])
            else:
                self.feed[followerId] = self.posts[followeeId]

            heapq.heapify(self.feed[followerId])
            

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 

        if followerId not in self.followers[followeeId]:
            return

        copy = []

        for i in self.feed[followerId]:
            if i[2] != followeeId:
                copy.append(i)

        self.followers[followeeId].remove(followerId)

        self.feed[followerId] = copy
        heapq.heapify(self.feed[followerId])
