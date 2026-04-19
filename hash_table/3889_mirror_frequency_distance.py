from collections import defaultdict, Counter
from string import ascii_lowercase, digits


class Solution:
    def mirrorFrequency(self, s: str) -> int:
        res = 0
        cnt = Counter(s)
        for i in range(13):
            res += abs(cnt[ascii_lowercase[i]] - cnt[ascii_lowercase[~i]])
        for i in range(5):
            res += abs(cnt[digits[i]] - cnt[digits[~i]])
        return res

    def mirrorFrequency1(self, s: str) -> int:
        cnt = defaultdict(int)
        for c in s:
            if c.isdigit():
                x = ord(c) - ord('0')
                if x < 5:
                    cnt[c] += 1
                else:
                    cnt[chr(ord('0') + 9 - x)] -= 1
            else:
                x = ord(c) - ord('a')
                if x < 13:
                    cnt[c] += 1
                else:
                    cnt[chr(ord('a') + 25 - x)] -= 1
        return sum(map(abs, cnt.values()))


def test_mirror_frequency():
    solution = Solution()
    assert solution.mirrorFrequency("ab1z9") == 3, 'wrong result'
    assert solution.mirrorFrequency("4m7n") == 2, 'wrong result'
    assert solution.mirrorFrequency("byby") == 0, 'wrong result'


if __name__ == '__main__':
    test_mirror_frequency()
