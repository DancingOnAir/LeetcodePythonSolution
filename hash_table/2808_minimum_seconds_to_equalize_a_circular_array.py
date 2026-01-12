from typing import List
from collections import defaultdict
from itertools import pairwise


class Solution:
    def minimumSeconds(self, nums: List[int]) -> int:
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        n = len(nums)
        res = n
        for v in pos.values():
            v.append(v[0] + n)
            cur = max(j - i for i, j in pairwise(v))
            res = min(res, cur)
        return res // 2


def test_minimum_seconds():
    solution = Solution()
    assert solution.minimumSeconds([1, 2, 1, 2]) == 1, 'wrong result'
    assert solution.minimumSeconds([2, 1, 3, 3, 2]) == 2, 'wrong result'
    assert solution.minimumSeconds([5, 5, 5, 5]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_seconds()
