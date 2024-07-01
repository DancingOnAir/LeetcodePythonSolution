from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum((x % 3) != 0 for x in nums)


def test_minimum_operations():
    solution = Solution()
    assert solution.minimumOperations([1,2,3,4]) == 3, 'wrong result'
    assert solution.minimumOperations([3,6,9]) == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_operations()
