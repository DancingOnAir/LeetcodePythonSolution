from functools import lru_cache


class Solution:
    #
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10 ** 9 + 7

        def helper(s):
            @lru_cache(None)
            def dp(i, sm, tight):
                if sm > max_sum:
                    return 0
                if i == len(s):
                    return sm >= min_sum

                res = 0
                up = int(s[i]) if tight else 9
                for d in range(up + 1):
                    res += dp(i + 1, sm + d, tight and d == up)
                return res % mod
            return dp(0, 0, True)
        return (helper(num2) - helper(str(int(num1) - 1))) % mod


def test_count():
    solution = Solution()
    assert solution.count("1", "12", 1, 8) == 11, 'wrong result'
    assert solution.count("1", "5", 1, 5) == 5, 'wrong result'


if __name__ == '__main__':
    test_count()
