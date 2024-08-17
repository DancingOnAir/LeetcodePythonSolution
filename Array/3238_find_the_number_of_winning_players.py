from typing import List
from collections import Counter


class Solution:
    # 找出重复的(x, y)
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        cnt = Counter(map(tuple, pick))
        return len({player for (player, _), x in cnt.items() if x > player})

    def winningPlayerCount1(self, n: int, pick: List[List[int]]) -> int:
        res = [Counter() for _ in range(n)]
        for x, y in pick:
            res[x][y] += 1

        return sum(1 for i in range(n) if res[i].most_common(1) and res[i].most_common(1)[0][1] > i)


def test_winning_player_count():
    solution = Solution()
    assert solution.winningPlayerCount(4, [[0, 0], [1, 0], [1, 0], [2, 1], [2, 1], [2, 0]]) == 2, 'wrong result'
    assert solution.winningPlayerCount(5, [[1, 1], [1, 2], [1, 3], [1, 4]]) == 0, 'wrong result'
    assert solution.winningPlayerCount(5, [[1, 1], [2, 4], [2, 4], [2, 4]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_winning_player_count()
