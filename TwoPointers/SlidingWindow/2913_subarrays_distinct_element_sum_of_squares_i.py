from typing import List
from collections import Counter


class Solution:
    # brute force
    def sumCounts(self, nums: List[int]) -> int:
        # cnt = Counter()
        n = len(nums)
        res = 0
        for i in range(n):
            for j in range(i, n):
                cnt = len(set(nums[i: j+1]))
                res += cnt ** 2
        return res


def test_sum_counts():
    solution = Solution()
    assert solution.sumCounts([1, 2, 1]) == 15, 'wrong result'
    assert solution.sumCounts([1, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_sum_counts()
