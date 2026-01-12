from typing import List
from collections import Counter
from itertools import combinations


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res, a, c = 0, 0, len(nums)
        cnt = Counter(nums)
        for b in cnt.values():
            c -= b
            res += a * b * c
            a += b
        return res

    def unequalTriplets1(self, nums: List[int]) -> int:
        res = 0
        cnt = Counter(nums)
        if len(cnt) < 3:
            return res

        for i, j, k in combinations(cnt, 3):
            res += cnt[i] * cnt[j] * cnt[k]
        return res


def test_unequal_triplets():
    solution = Solution()
    assert solution.unequalTriplets([4, 4, 2, 4, 3]) == 3, 'wrong result'
    assert solution.unequalTriplets([1, 1, 1, 1, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_unequal_triplets()
