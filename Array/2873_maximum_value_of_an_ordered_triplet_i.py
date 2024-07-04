from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = maxab = maxa = 0
        for x in nums:
            res = max(res, maxab * x)
            maxab = max(maxab, maxa - x)
            maxa = max(maxa, x)
        return res

    def maximumTripletValue1(self, nums: List[int]) -> int:
        res, n = 0, len(nums)
        left_max = [0] * n
        mx = 0
        for i in range(1, n):
            mx = max(mx, nums[i - 1])
            left_max[i] = mx

        right_max = [0] * n
        mx = 0
        for i in range(n - 2, -1, -1):
            mx = max(mx, nums[i + 1])
            right_max[i] = mx

        res = 0
        for i in range(1, n - 1):
            if left_max[i] < nums[i]:
                continue
            res = max(res, (left_max[i] - nums[i]) * right_max[i])
        return res


def test_maximum_triplet_value():
    solution = Solution()
    assert solution.maximumTripletValue([12, 6, 1, 2, 7]) == 77, 'wrong result'
    assert solution.maximumTripletValue([1, 10, 3, 4, 19]) == 133, 'wrong result'
    assert solution.maximumTripletValue([1, 2, 3]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_triplet_value()
