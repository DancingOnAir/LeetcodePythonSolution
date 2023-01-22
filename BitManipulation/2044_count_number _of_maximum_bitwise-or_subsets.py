from typing import List
from collections import Counter, defaultdict
from itertools import zip_longest


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        m = defaultdict(int)
        for i in range(1, 1 << len(nums)):
            total = 0
            for j in range(len(nums)):
                if (i & (1 << j)) > 0:
                    total |= nums[j]
            m[total] += 1
        return m[max(m)]


def test_count_max_or_subsets():
    solution = Solution()
    assert solution.countMaxOrSubsets([3,1]) == 2, 'wrong result'
    assert solution.countMaxOrSubsets([2,2,2]) == 7, 'wrong result'
    assert solution.countMaxOrSubsets([3,2,1,5]) == 6, 'wrong result'


if __name__ == '__main__':
    test_count_max_or_subsets()
