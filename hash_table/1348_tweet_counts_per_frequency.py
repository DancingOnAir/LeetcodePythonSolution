from typing import List
from bisect import bisect_left, bisect_right


class TweetCounts:
    def __init__(self):
        self.tweets = dict()

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets.setdefault(tweetName, []).append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == "minute":
            seconds = 60
        elif freq == "hour":
            seconds = 3600
        else:
            seconds = 86400

        res = [0] * ((endTime - startTime) // seconds + 1)
        for t in self.tweets[tweetName]:
            if startTime <= t <= endTime:
                res[(t - startTime) // seconds] += 1
        return res


def test_tweet_counts():
    tweetCounts = TweetCounts()
    tweetCounts.recordTweet("tweet3", 0)
    tweetCounts.recordTweet("tweet3", 60)
    tweetCounts.recordTweet("tweet3", 10)
    assert tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59) == [2], 'wrong result'
    assert tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60) == [2, 1], 'wrong result'
    tweetCounts.recordTweet("tweet3", 120)
    assert tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210) == [4], 'wrong result'


if __name__ == '__main__':
    test_tweet_counts()
