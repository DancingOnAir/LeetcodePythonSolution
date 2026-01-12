from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n, res = len(nums), float('inf')
        mi, suf = nums[-1], [0] * n

        for i in range(n - 2, 0, -1):
            if nums[i] > mi:
                suf[i] = mi
            elif nums[i] < mi:
                mi = nums[i]

        mi = nums[0]
        for i in range(1, n - 1):
            if nums[i] > mi:
                if suf[i] and res > mi + nums[i] + suf[i]:
                    res = mi + nums[i] + suf[i]
            elif nums[i] < mi:
                mi = nums[i]
        return res if res < float('inf') else -1


def test_minimum_sum():
    solution = Solution()
    assert solution.minimumSum([8, 6, 1, 5, 3]) == 9, 'wrong result'
    assert solution.minimumSum([5, 4, 8, 7, 10, 2]) == 13, 'wrong result'
    assert solution.minimumSum([6, 5, 4, 3, 4, 5]) == -1, 'wrong result'


if __name__ == '__main__':
    test_minimum_sum()
