from typing import List
import bisect


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        min_nums = [nums[0]]
        for i in range(1, n):
            min_nums.append(min(min_nums[-1], nums[i]))

        stk = []
        for i in range(n - 1, -1, -1):
            if nums[i] > min_nums[i]:
                while stk and stk[-1] <= min_nums[i]:
                    stk.pop()
                if stk and nums[i] > stk[-1]:
                    return True
                stk.append(nums[i])

        return False


def test_find_132_pattern():
    solution = Solution()

    nums1 = [1, 2, 3, 4]
    print(solution.find132pattern(nums1))

    nums2 = [3, 1, 4, 2]
    print(solution.find132pattern(nums2))

    nums3 = [-1, 3, 2, 0]
    print(solution.find132pattern(nums3))

    nums4 = [1, 0, 1, -4, -3]
    print(solution.find132pattern(nums4))


if __name__ == '__main__':
    test_find_132_pattern()
