from typing import List
from bisect import bisect_left


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        seen = set()
        res = -1
        for x in nums:
            if x in seen:
                continue

            temp = {x}
            while True:
                idx = bisect_left(nums, x ** 2)
                if idx < len(nums) and nums[idx] == x ** 2:
                    temp.add(nums[idx])
                    x = nums[idx]
                else:
                    break
            if len(temp) > 1:
                res = max(res, len(temp))
            seen |= temp
        return res

    def longestSquareStreak1(self, nums: List[int]) -> int:
        def binary_search(i):
            l, r = i + 1, len(nums) - 1
            k = nums[i] ** 2
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < k:
                    l = mid + 1
                elif nums[mid] > k:
                    r = mid - 1
                else:
                    return mid
            return -1

        nums.sort()
        seen = set()
        res = -1
        for i, v in enumerate(nums):
            if v not in seen:
                temp = {v}
                cur = binary_search(i)
                while cur != -1:
                    temp.add(nums[cur])
                    cur = binary_search(cur)
                if len(temp) > 1:
                    res = max(res, len(temp))
                seen.union(temp)
        return res


def test_longest_square_streak():
    solution = Solution()
    assert solution.longestSquareStreak([4, 3, 6, 16, 8, 2]) == 3, 'wrong result'
    assert solution.longestSquareStreak([2, 3, 5, 6, 7]) == -1, 'wrong result'


if __name__ == '__main__':
    test_longest_square_streak()
