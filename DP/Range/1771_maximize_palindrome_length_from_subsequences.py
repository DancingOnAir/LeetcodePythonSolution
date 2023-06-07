from functools import lru_cache


class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        res = 0
        n = len(s)

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1

            if s[i] == s[j]:
                cur = dfs(i + 1, j - 1) + 2
                # 最终结果一定要包含word1[i]和word2[j]
                nonlocal res
                if i < len(word1) <= j:
                    res = max(res, cur)
                return cur

            return max(dfs(i + 1, j), dfs(i, j - 1))

        dfs(0, n - 1)
        return res


def test_longest_palindrome():
    solution = Solution()
    assert solution.longestPalindrome("cfe", "ef") == 4, 'wrong result'
    assert solution.longestPalindrome("cacb", "cbba") == 5, 'wrong result'
    assert solution.longestPalindrome("ab", "ab") == 3, 'wrong result'
    assert solution.longestPalindrome("aa", "bb") == 0, 'wrong result'


if __name__ == '__main__':
    test_longest_palindrome()
