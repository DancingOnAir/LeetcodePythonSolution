from functools import lru_cache


class Solution:
    def maxProduct(self, s: str) -> int:
        def is_palidrome(x):
            return x == x[::-1]

        @lru_cache(None)
        def dfs(s, s1, s2, idx):
            nonlocal res
            if is_palidrome(s1) and is_palidrome(s2):
                res = max(res, len(s1) * len(s2))
            if idx == n:
                return

            dfs(s, s1+s[idx], s2, idx+1)
            dfs(s, s1, s2+s[idx], idx+1)
            dfs(s, s1, s2, idx+1)

        res = 0
        dfs(s, '', '', 0)
        return res


def test_max_product():
    solution = Solution()
    assert solution.maxProduct("leetcodecom") == 9, 'wrong result'
    assert solution.maxProduct("bb") == 1, 'wrong result'
    assert solution.maxProduct("accbcaxxcxx") == 25, 'wrong result'


if __name__ == '__main__':
    test_max_product()
