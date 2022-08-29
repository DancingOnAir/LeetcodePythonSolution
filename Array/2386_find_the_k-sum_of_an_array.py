from typing import List
from itertools import combinations


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = list()
        for i in range(n + 1):
            for c in combinations(nums, i):
                res.append(sum(c))
        return sorted(res)[-k]


def test_k_sum():
    solution = Solution()
    assert solution.kSum([2, 4, -2], 5) == 2, 'wrong result'
    assert solution.kSum([1, -2, 3, 4, -10, 12], 16) == 10, 'wrong result'


if __name__ == '__main__':
    test_k_sum()
