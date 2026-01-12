from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        res = 0
        for x in nums:
            res += abs(x - sum(map(int, str(x))))
        return res


def test_difference_of_sum():
    solution = Solution()
    assert solution.differenceOfSum([1, 15, 6, 3]) == 9, 'wrong result'
    assert solution.differenceOfSum([1, 2, 3, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_difference_of_sum()
