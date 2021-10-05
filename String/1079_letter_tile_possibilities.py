from collections import Counter
from math import comb


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c = Counter(tiles)
        l = 0
        # dp[i][j] represents the possibilities of first i+1 items in counter, length equals j
        # dp[i][0] = 1
        dp = [1] + [0] * len(tiles)
        for v in c.values():
            l += v
            for i in range(l, 0, -1):
                dp[i] += sum(dp[i - j] * comb(i, j) for j in range(1, min(i, v) + 1))
        return sum(dp) - 1


def test_num_tile_possibilities():
    solution = Solution()
    # for 1 char: 2, for 2 chars: 3, for 3 chars: 3
    assert solution.numTilePossibilities("AAB") == 8, 'wrong result'
    # for 1 char: 3, for 2 chars: 3 + 3 + 2, for 3 chars:
    assert solution.numTilePossibilities("AAABBC") == 188, 'wrong result'
    assert solution.numTilePossibilities("V") == 1, 'wrong result'


if __name__ == '__main__':
    test_num_tile_possibilities()
