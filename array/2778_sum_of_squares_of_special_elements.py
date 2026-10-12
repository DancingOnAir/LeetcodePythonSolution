class Solution:
    def sumOfSquares(self, nums: list[int]) -> int:
        return sum(x * x for i, x in enumerate(nums) if len(nums) % (i + 1) == 0)


def test_sum_of_squares():
    solution = Solution()
    assert solution.sumOfSquares([1, 2, 3, 4]) == 21, 'wrong result'
    assert solution.sumOfSquares([2, 7, 1, 19, 18, 3]) == 63, 'wrong result'


if __name__ == '__main__':
    test_sum_of_squares()
