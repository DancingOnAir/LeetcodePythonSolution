from typing import List
from collections import Counter


class Solution:
    # http://leetcode.com/problems/stone-game-ix/solutions/1500245/javacpython-easy-and-concise-6-lines-on-47xlq/
    # If Alice starts with 1, then she needs 2 to win.
    # If Alice starts with 2, then she needs 1 to win.
    # Since Alice gets to pick first and she plays optimally, she'll pick 2 first if there are more 1's (and vice versa).
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = Counter(x % 3 for x in stones)
        if cnt[0] % 2 == 0:
            return cnt[1] > 0 and cnt[2] > 0
        return abs(cnt[1] - cnt[2]) > 2


def test_stone_game_ix():
    solution = Solution()
    assert not solution.stoneGameIX([1]), 'wrong result'
    assert solution.stoneGameIX([2, 1]), 'wrong result'
    assert not solution.stoneGameIX([2]), 'wrong result'
    assert not solution.stoneGameIX([5, 1, 2, 4, 3]), 'wrong result'


if __name__ == '__main__':
    test_stone_game_ix()
