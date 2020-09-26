from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        pre_sum, res = 0, 1
        for i, val in enumerate(nums):
            pre_sum += val
            res = max(res, 1 - pre_sum)
        return res


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
