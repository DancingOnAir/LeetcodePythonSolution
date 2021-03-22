class Solution:
    # dp
    def countSubstrings(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        # same_dp[i][j]: The same subStr count at i of s and j of t
        same_dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        # diff_dp[i][j]: The 1 char diff subStr count at i of s and j of t
        diff_dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1):
            for j in range(l2):
                same_dp[i + 1][j + 1] = same_dp[i][j] + 1 if s[i] == t[j] else 0

        for i in range(l1):
            for j in range(l2):
                diff_dp[i + 1][j + 1] = diff_dp[i][j] if s[i] == t[j] else same_dp[i][j] + 1

        res = 0
        for i in range(l1 + 1):
            res += sum(diff_dp[i])
        return res

    # brute force
    def countSubstrings1(self, s: str, t: str) -> int:
        l1, l2 = len(s), len(t)
        res = 0

        for i in range(l1):
            for j in range(l2):
                diff = 0
                k = 0
                while i + k < l1 and j + k < l2:
                    if s[i + k] != t[j + k]:
                        diff += 1

                    if diff == 1:
                        res += 1
                    elif diff == 2:
                        break
                    k += 1

        return res


def test_count_substrings():
    solution = Solution()
    assert solution.countSubstrings('aba', 'baba') == 6, 'wrong result'
    assert solution.countSubstrings('ab', 'bb') == 3, 'wrong result'
    assert solution.countSubstrings('a', 'a') == 0, 'wrong result'
    assert solution.countSubstrings('abe', 'bbc') == 10, 'wrong result'


if __name__ == '__main__':
    test_count_substrings()
