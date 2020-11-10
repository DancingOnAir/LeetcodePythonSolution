from typing import List


class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        def isUnhappyFriend(pair: List[int]) -> bool:
            for friend in preferences[p[0]][:preferences[p[0]].index(p[1])]:
                if p[0] in preferences[friend][:preferences[friend].index(relationships[friend])]:
                    return True
            return False

        relationships = dict()
        for p in pairs:
            relationships[p[0]] = p[1]
            relationships[p[1]] = p[0]

        res = 0
        for p in pairs:
            if isUnhappyFriend(p):
                res += 1
            if isUnhappyFriend(p.reverse()):
                res += 1
        return res


def test_unhappy_friends():
    solution = Solution()

    n1 = 4
    preferences1 = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    pairs1 = [[0, 1], [2, 3]]
    assert solution.unhappyFriends(n1, preferences1, pairs1) == 2, "wrong result"

    n2 = 2
    preferences2 = [[1], [0]]
    pairs2 = [[1, 0]]
    assert solution.unhappyFriends(n2, preferences2, pairs2) == 0, "wrong result"

    n3 = 4
    preferences3 = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
    pairs3 = [[1, 3], [0, 2]]
    assert solution.unhappyFriends(n3, preferences3, pairs3) == 4, "wrong result"


if __name__ == '__main__':
    test_unhappy_friends()
