class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s == 0:
            return 0
        if n * 9 < s:
            return -1

        res = 10 ** (s // 9) - 1
        if s % 9:
            res = res * 10 + s % 9
            n -= 1
        return res * 10 ** (n - s // 9)

def test_largest_integer():
    solution = Solution()
    assert solution.largestInteger(2, 9) == 90, 'wrong result'
    assert solution.largestInteger(2, 19) == -1, 'wrong result'
    assert solution.largestInteger(5, 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_largest_integer()
