class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)


def test_min_moves():
    solution = Solution()
    assert solution.minMoves2([1, 2, 3]) == 2, 'wrong result'
    assert solution.minMoves2([1, 10, 2, 9]) == 16, 'wrong result'


if __name__ == '__main__':
    test_min_moves()
