from typing import List
from math import ceil


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            if x in seen:
                return i // 3 + 1
            seen.add(x)
        return 0

    def minimumOperations1(self, nums: List[int]) -> int:
        m = set()
        for i, x in enumerate(nums[::-1]):
            if x in m:
                return ceil((len(nums) - i) / 3)
            m.add(x)
        return 0


def test_minimum_operations():
    solution = Solution()
    # assert solution.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]) == 2, 'wrong result'
    assert solution.minimumOperations([4, 5, 6, 4, 4]) == 2, 'wrong result'
    assert solution.minimumOperations([6, 7, 8, 9]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations()
