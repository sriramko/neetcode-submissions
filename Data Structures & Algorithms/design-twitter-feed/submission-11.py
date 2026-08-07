class Twitter:

    def __init__(self):
        self.following = dict() # follower -> followees
        self.tweets = dict() # user -> timestamps heap
        self.timestamps = dict() # timestamps -> tweets
        self.timeId = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.following:
            self.following[userId] = set()
            self.tweets[userId] = [self.timeId]
            self.timestamps[self.timeId] = tweetId
        else:
            heapq.heappush(self.tweets[userId],self.timeId)
            self.timestamps[self.timeId] = tweetId
        self.timeId -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.following:
            self.following[userId] = set()
            self.tweets[userId] = []
        candidates = []
        for friend in self.following[userId]:
            candidates = heapq.merge(candidates,heapq.nsmallest(10,self.tweets[friend]))
        candidates = heapq.merge(candidates,heapq.nsmallest(10,self.tweets[userId]))
        res = list(candidates)[:10]
        return [self.timestamps[time] for time in res]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = {followeeId}
            self.tweets[followerId] = []
        else:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()
            self.tweets[followerId] = []
        self.following[followerId].discard(followeeId)
