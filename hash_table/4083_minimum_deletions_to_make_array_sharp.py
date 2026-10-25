from itertools import groupby


class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        return sum(max(0, len(list(g)) - 1) for _, g in groupby(nums))


def test_min_deletions():
    solution = Solution()
    assert solution.minDeletions([1, 1, 2, 2, 2, 3]) == 3, 'wrong result'
    assert solution.minDeletions([4, 4, 9, 4]) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_deletions()
