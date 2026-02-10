from typing import List
from collections import defaultdict


class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        return len({a for a, b in zip(nums, target) if a != b})

    def minOperations1(self, nums: List[int], target: List[int]) -> int:
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            if x == target[i]:
                continue
            cnt[x] += 1

        return len(cnt)


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 2, 3], target=[2, 1, 3]) == 2, 'wrong result'
    assert solution.minOperations([4, 1, 4], target=[5, 1, 4]) == 1, 'wrong result'
    assert solution.minOperations([7, 3, 7], target=[5, 5, 9]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
