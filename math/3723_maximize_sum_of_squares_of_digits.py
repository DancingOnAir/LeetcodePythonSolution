class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        q, r = divmod(sum, 9)
        extra = 1 if r > 0 else 0
        if q + extra > num:
            return ""
        res = '9' * q
        if extra > 0:
            res += str(r)
        return res + '0' * (num - q - extra)


def test_max_sum_of_squares():
    solution = Solution()
    assert solution.maxSumOfSquares(2, 3) == "30", 'wrong result'
    assert solution.maxSumOfSquares(2, 17) == "98", 'wrong result'
    assert solution.maxSumOfSquares(1, 10) == "", 'wrong result'


if __name__ == '__main__':
    test_max_sum_of_squares()
