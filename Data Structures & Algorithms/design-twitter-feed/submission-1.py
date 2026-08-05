class User:
    def __init__(self, userId):
        self.userId = userId
        self.following = {}
        self.followers = {}

    def follow(self, user):
        self.following[user.userId] = user

    def unfollow(self, user):
        del self.following[user.userId]

    def addFollower(self, follower):
        self.followers[follower.userId] = follower

    def removeFollower(self, follower):
        del self.followers[follower.userId]

class Tweet:
    def __init__(self, tweetId, authorId):
        self.tweetId = tweetId
        self.authorId = authorId

class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = [] # Stack

    def createUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.createUser(userId)

        self.tweets.append(Tweet(tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        self.createUser(userId)

        newsFeed = []

        for i in range(len(self.tweets)-1, -1, -1):
            if self.tweets[i].authorId in self.users[userId].following or self.tweets[i].authorId == userId:
                newsFeed.append(self.tweets[i].tweetId)
            if len(newsFeed) >= 10:
                break

        return newsFeed


    def follow(self, followerId: int, followeeId: int) -> None:
        self.createUser(followerId)
        self.createUser(followeeId)

        self.users[followeeId].followers[followerId] = self.users[followerId]
        self.users[followerId].following[followeeId] = self.users[followeeId]

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users[followeeId].followers:
            del self.users[followeeId].followers[followerId]
            del self.users[followerId].following[followeeId]
