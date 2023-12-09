class Solution:
    # dp[i] means the minimum value of subsequence with length
    def longestSubsequence2(self, s: str, k: int) -> int:
        dp = [0]
        for v in map(int, s):
            if dp[-1] * 2 + v <= k:
                dp.append(dp[-1] * 2 + v)
            for i in range(len(dp) - 1, 0, -1):
                dp[i] = min(dp[i], dp[i - 1] * 2 + v)
        return len(dp) - 1

    def longestSubsequence(self, s: str, k: int) -> int:
        k = bin(k)[2:]
        if len(s) < len(k):
            return len(s)
        res = s[:-len(k)].count('0') + len(k)
        if s[-len(k):] <= k:
            return res
        return res - 1

    def longestSubsequence1(self, s: str, k: int) -> int:
        res = len(s)
        if int(s, 2) <= k:
            return res

        s = list(s)
        for i, ch in enumerate(s):
            if ch == '1':
                s[i] = ''
                res -= 1
                if int(''.join(s), 2) <= k:
                    return res
        return res


def test_longest_subsequence():
    solution = Solution()
    assert solution.longestSubsequence("1001010", 5) == 5, 'wrong result'
    assert solution.longestSubsequence("00101001", 1) == 6, 'wrong result'


if __name__ == '__main__':
    test_longest_subsequence()
