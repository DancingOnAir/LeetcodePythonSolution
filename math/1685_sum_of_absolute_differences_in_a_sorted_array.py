from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        tot = sum(nums)
        ps = 0
        n = len(nums)
        res = []
        for i, x in enumerate(nums):
            tot -= x
            res.append(tot - (n - i - 1) * x + i * x - ps)
            ps += x
        return res


def test_get_sum_absolute_differences():
    solution = Solution()
    assert solution.getSumAbsoluteDifferences([2, 3, 5]) == [4, 3, 5], 'wrong result'
    assert solution.getSumAbsoluteDifferences([1, 4, 6, 8, 10]) == [24, 15, 13, 15, 21], 'wrong result'


if __name__ == '__main__':
    test_get_sum_absolute_differences()
