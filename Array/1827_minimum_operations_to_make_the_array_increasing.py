from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        res = 0
        for i in range(1, len(nums)):
            cur = max(nums[i - 1] + 1, nums[i])
            res += cur - nums[i]
            nums[i] = cur
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([1, 1, 1]) == 3, 'wrong result'
    assert solution.minOperations([1, 5, 2, 4, 1]) == 14, 'wrong result'
    assert solution.minOperations([8]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_operations()

