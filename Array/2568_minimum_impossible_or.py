from typing import List


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        for i in range(32):
            if (1 << i) not in set(nums):
                return 1 << i
        return 1 << 32


def test_min_impossible_or():
    solution = Solution()
    assert solution.minImpossibleOR([2, 1]) == 4, 'wrong result'
    assert solution.minImpossibleOR([5, 3, 2]) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_impossible_or()
