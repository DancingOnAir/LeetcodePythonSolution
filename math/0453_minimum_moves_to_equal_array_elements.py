class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mi = min(nums)
        return sum(x - mi for x in nums)


def test_min_moves():
    solution = Solution()
    assert solution.minMoves([1, 2, 3]) == 3, 'wrong result'
    assert solution.minMoves([1, 1, 1]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_moves()
