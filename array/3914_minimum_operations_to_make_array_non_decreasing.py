from itertools import pairwise


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return sum(a - b for a, b in pairwise(nums) if a > b)


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([3, 3, 2, 1]) == 2, 'wrong result'
    assert solution.minOperations([5, 1, 2, 3]) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
