from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_left(i):
            end = nums[-1]
            if nums[i] > end:
                return nums[i] >= target > end
            else:
                return target > end or target <= nums[i]

        # (-1, n)
        left, right = -1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if is_left(mid):
                right = mid
            else:
                left = mid
        if right == len(nums) or nums[right] != target:
            return -1
        return right


def test_search():
    solution = Solution()
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4, 'wrong result'
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1, 'wrong result'
    assert solution.search([1], 0) == -1, 'wrong result'


if __name__ == '__main__':
    test_search()
