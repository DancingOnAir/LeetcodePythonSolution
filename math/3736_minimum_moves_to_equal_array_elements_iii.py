class Solution:
    def minMoves(self, nums: list[int]) -> int:
        return len(nums) * max(nums) - sum(nums)


def test_min_moves():
    solution = Solution()
    assert solution.minMoves([2, 1, 3]) == 3, 'wrong result'
    assert solution.minMoves([4, 4, 5]) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_moves()
