from typing import List
from bisect import bisect_left
from math import ceil


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        res = list()
        for s in spells:
            s = ceil(success / s)
            res.append(n - bisect_left(potions, s))
        return res


def test_successful_pairs():
    solution = Solution()
    assert solution.successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7) == [4, 0, 3]
    assert solution.successfulPairs([3, 1, 2], [8, 5, 8], 16) == [2, 0, 2]


if __name__ == '__main__':
    test_successful_pairs()
