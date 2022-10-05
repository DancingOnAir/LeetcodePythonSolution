from typing import List
from bisect import bisect_left


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse=True)
        trainers.sort()
        res = 0

        for t in trainers:
            if players and players[-1] <= t:
                res += 1
                players.pop()
        return res

    def matchPlayersAndTrainers2(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        l1, l2 = len(players), len(trainers)
        res = i = j = 0

        while i < l1 and j < l2:
            while j < l2 and trainers[j] < players[i]:
                j += 1
            if j < l2:
                res += 1
            i += 1
            j += 1
        return res

    # TLE, 不需要二分查找
    def matchPlayersAndTrainers1(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        res = 0
        i, pre = -1, 0
        for p in players:
            pre += i + 1
            i = bisect_left(trainers[pre:], p)
            if i + pre >= len(trainers):
                break
            res += 1
        return res


def test_match_players_and_trainers():
    solution = Solution()
    assert solution.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8]) == 2, 'wrong result'
    assert solution.matchPlayersAndTrainers([1, 1, 1], [10]) == 1, 'wrong result'


if __name__ == '__main__':
    test_match_players_and_trainers()

