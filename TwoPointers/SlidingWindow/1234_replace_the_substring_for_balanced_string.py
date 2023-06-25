from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
        m = len(s) // 4
        cnt = Counter(s)
        if all(cnt[ch] == m for ch in 'QWER'):
            return 0

        res = len(s)
        left = 0
        for right, ch in enumerate(s):
            cnt[ch] -= 1
            while all(cnt[x] <= m for x in 'QWER'):
                res = min(res, right - left + 1)
                cnt[s[left]] += 1
                left += 1
        return res


def test_balanced_string():
    solution = Solution()
    assert solution.balancedString("QWER") == 0, 'wrong result'
    assert solution.balancedString("QQWE") == 1, 'wrong result'
    assert solution.balancedString("QQQW") == 2, 'wrong result'


if __name__ == '__main__':
    test_balanced_string()
