from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums) - {0})

    def minimumOperations1(self, nums: List[int]) -> int:
        return len(set(nums)) - (1 if 0 in set(nums) else 0)


def test_minimum_operations():
    solution = Solution()
    assert solution.minimumOperations([1, 5, 0, 3, 5]) == 3, 'wrong result'
    assert solution.minimumOperations([0]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations()
