from collections import Counter, defaultdict


class Solution:
    def balancedString(self, s: str) -> int:
        extra = Counter(s) - Counter({c: len(s) // 4 for c in 'QWER'})
        if not extra:
            return 0

        res = len(s)
        indices = defaultdict(list)
        for i, c in enumerate(s):
            indices[c].append(i)
            if any(len(indices[k]) < v for k, v in extra.items()):
                continue

            res = min(res, i - min(indices[k][-v] for k, v in extra.items()) + 1)
        return res

    # sliding window
    def balancedString1(self, s: str) -> int:
        res = n = len(s)
        count = Counter(s)
        if all(x == n // 4 for x in count.values()):
            return 0

        i = 0
        for j, c in enumerate(s):
            count[c] -= 1
            while i < n and all(n / 4 >= count[x] for x in 'QWER'):
                res = min(res, j - i + 1)
                count[s[i]] += 1
                i += 1
        return res


def test_balanced_string():
    solution = Solution()

    assert solution.balancedString("WQWRQQQW") == 3, 'wrong result'
    assert solution.balancedString('QWER') == 0, 'wrong result'
    assert solution.balancedString('QQWE') == 1, 'wrong result'
    assert solution.balancedString('QQQW') == 2, 'wrong result'
    assert solution.balancedString('QQQQ') == 3, 'wrong result'


if __name__ == '__main__':
    test_balanced_string()
