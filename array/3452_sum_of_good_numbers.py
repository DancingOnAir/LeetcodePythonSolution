from typing import List


class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        res = 0
        for i, x in enumerate(nums):
            if (i - k >= 0 and nums[i - k] >= x) or (i + k < len(nums) and nums[i + k] >= x):
                continue
            res += x
        return res


def test_sum_of_good_numbers():
    solution = Solution()
    assert solution.sumOfGoodNumbers([1, 3, 2, 1, 5, 4], k=2) == 12, 'wrong result'
    assert solution.sumOfGoodNumbers([2, 1], k=1) == 2, 'wrong result'


if __name__ == '__main__':
    test_sum_of_good_numbers()
