from typing import List


class Solution:
    def minIncrementOperations(self, nums: List[int], k: int) -> int:
        res, n = 0, len(nums)
        for i in range(n - 2):
            mx = max(nums[i], nums[i + 1], nums[i + 2])
            if mx < k:
                diff = k - mx
                res += diff
                nums[i] += diff
                nums[i + 1] += diff
                nums[i + 2] += diff

        return res


def test_min_increment_operations():
    solution = Solution()
    assert solution.minIncrementOperations([43, 31, 14, 4], 73) == 42, 'wrong result'
    assert solution.minIncrementOperations([0, 1, 3, 3], 5) == 2, 'wrong result'
    assert solution.minIncrementOperations([2, 3, 0, 0, 2], 4) == 3, 'wrong result'
    assert solution.minIncrementOperations([1, 1, 2], 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_increment_operations()
