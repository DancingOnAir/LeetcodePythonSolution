from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)
        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        res = n
        # 注意头尾的不行
        for i in range(1, n - 1):
            if left[i] > 1 and right[i] > 1:
                res = min(res, n - left[i] - right[i] + 1)
        return res


def test_minimum_mountain_removals():
    solution = Solution()
    assert solution.minimumMountainRemovals([100, 92, 89, 77, 74, 66, 64, 66, 64]) == 6, 'wrong result'
    assert solution.minimumMountainRemovals([9, 8, 1, 7, 6, 5, 4, 3, 2, 1]) == 2, 'wrong result'
    assert solution.minimumMountainRemovals([1, 3, 1]) == 0, 'wrong result'
    assert solution.minimumMountainRemovals([2, 1, 1, 5, 6, 2, 3, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_mountain_removals()
