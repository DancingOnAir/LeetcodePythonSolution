class Solution:
    def minimumSteps(self, s: str) -> int:
        res = n = 0
        for i, c in enumerate(s):
            if c == '0':
                n += 1
                res += i
        return res - (n - 1) * n // 2


def test_minimum_steps():
    solution = Solution()
    assert solution.minimumSteps("101") == 1, 'wrong result'
    assert solution.minimumSteps("100") == 2, 'wrong result'
    assert solution.minimumSteps("0111") == 0, 'wrong result'


if __name__ == '__main__':
    test_minimum_steps()
