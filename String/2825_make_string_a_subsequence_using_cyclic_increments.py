from functools import lru_cache


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        l1, l2 = len(str1), len(str2)

        @lru_cache(None)
        def dfs(i, j):
            if j == l2:
                return True

            if i == l1:
                return False

            for k in range(i, len(str1)):
                if l1 - k < l2 - j:
                    break

                nxt = chr((ord(str1[k]) - 96) % 26 + ord('a'))
                if str1[k] == str2[j] or nxt == str2[j]:
                    if dfs(k + 1, j + 1):
                        return True
            return False

        return dfs(0, 0)


def test_can_make_subsequence():
    solution = Solution()
    assert solution.canMakeSubsequence("abc", "ad"), 'wrong result'
    assert solution.canMakeSubsequence("zc", "ad"), 'wrong result'
    assert not solution.canMakeSubsequence("ab", "d"), 'wrong result'


if __name__ == '__main__':
    test_can_make_subsequence()
