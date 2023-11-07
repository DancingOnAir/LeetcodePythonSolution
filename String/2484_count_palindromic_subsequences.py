class Solution:
    # https://leetcode.com/problems/count-palindromic-subsequences/solutions/2850466/c-java-python3-counting-prefixes-and-suffixes/
    def countPalindromes(self, s: str) -> int:
        mod = 10 ** 9 + 7
        n = len(s)
        pre, cnt = [[[0] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n):
            c = ord(s[i]) - ord('0')
            if i:
                for j in range(10):
                    for k in range(10):
                        pre[i][j][k] = pre[i - 1][j][k]
                        if k == c:
                            pre[i][j][k] += cnt[j]
            cnt[c] += 1

        suf, cnt = [[[0] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('0')
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suf[i][j][k] = suf[i + 1][j][k]
                        if k == c:
                            suf[i][j][k] += cnt[j]
            cnt[c] += 1

        res = 0
        for i in range(2, n - 2):
            for j in range(10):
                for k in range(10):
                    res += pre[i - 1][j][k] * suf[i + 1][j][k]
        return res % mod


def test_count_palindromes():
    solution = Solution()
    assert solution.countPalindromes("103301") == 2, 'wrong result'
    assert solution.countPalindromes("0000000") == 21, 'wrong result'
    assert solution.countPalindromes("9999900000") == 2, 'wrong result'


if __name__ == '__main__':
    test_count_palindromes()
