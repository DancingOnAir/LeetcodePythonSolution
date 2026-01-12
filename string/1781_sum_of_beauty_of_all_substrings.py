from collections import defaultdict
from copy import deepcopy
from collections import Counter


class Solution:
    # Counter + memo
    def beautySum(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            c = Counter()
            for j in range(i, len(s)):
                c[s[j]] += 1
                res += max(c.values()) - min(c.values())

        return res

    # frequency table
    def beautySum2(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            freq = [0] * 26
            for j in range(i, len(s)):
                freq[ord(s[j]) - 97] += 1
                res += max(freq) - min(x for x in freq if x)

        return res

    # brute force by Counter, but TlE
    def beautySum1(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        res = 0
        for i in range(n - 2):
            for j in range(2, n - i + 1):
                c = Counter(s[i: i + j])
                res += c.most_common()[0][1] - c.most_common()[-1][1]

        return res


def test_beauty_sum():
    solution = Solution()
    assert solution.beautySum('aabcb') == 5, 'wrong result'
    assert solution.beautySum('aabcbaa') == 17, 'wrong result'


if __name__ == '__main__':
    test_beauty_sum()
