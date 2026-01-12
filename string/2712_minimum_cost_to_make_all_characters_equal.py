class Solution:
    def minimumCost(self, s: str) -> int:
        res, n = 0, len(s)
        for i in range(1, n):
            if s[i - 1] != s[i]:
                res += min(i, n - i)
        return res


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost("0011") == 2, 'wrong result'
    assert solution.minimumCost("010101") == 9, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
