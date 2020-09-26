from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        s, res = 0, float('inf')
        for i, val in enumerate(nums):
            s += val
            res = min(res, s)
        return 1 if res > 0 else -res + 1


def test_min_start_value():
    solution = Solution()

    nums1 = [-3, 2, -3, 4, 2]
    print(solution.minStartValue(nums1))

    nums2 = [1, 2]
    print(solution.minStartValue(nums2))

    nums3 = [1, -2, -3]
    print(solution.minStartValue(nums3))


if __name__ == '__main__':
    test_min_start_value()
