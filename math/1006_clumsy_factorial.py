class Solution:
    # N - (N - 1) * (N - 2) / (N - 3) = - 2 / (N - 3)
    # - 2 / (N - 3) = 0, If N - 3 > 2.
    # So when N > 5, N - (N - 1) * (N - 2) / (N - 3) = 0
    def clumsy(self, n: int) -> int:
        def helper(x):
            if x == 0:
                return 0
            if x == 1:
                return 1
            if x == 2:
                return 1
            if x == 3:
                return 1
            if x == 4:
                return -2
            if x == 5:
                return 0
            return helper((x - 2) % 4 + 2)

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        return n * (n - 1) // (n - 2) + helper(n - 3)


def test_clumsy():
    solution = Solution()
    assert solution.clumsy(4) == 7, 'wrong result'
    assert solution.clumsy(10) == 12, 'wrong result'


if __name__ == '__main__':
    test_clumsy()
