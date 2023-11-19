class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            dp[i] = max(dp[max(0, i - k): min(25, i + k + 1)]) + 1
        return max(dp)

    # https://leetcode.com/problems/longest-ideal-subsequence/solutions/2390512/java-c-python-dp-solution/
    def longestIdealString1(self, s: str, k: int) -> int:
        dp = [0] * 128
        for c in s:
            i = ord(c)
            dp[i] = max(dp[i - k: i + k + 1]) + 1
        return max(dp)


def test_longest_ideal_string():
    solution = Solution()
    assert solution.longestIdealString("acfgbd", 2) == 4, 'wrong result'
    assert solution.longestIdealString("abcd", 3) == 4, 'wrong result'


if __name__ == '__main__':
    test_longest_ideal_string()
