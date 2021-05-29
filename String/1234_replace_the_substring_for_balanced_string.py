from collections import Counter


class Solution:
    def balancedString(self, s: str) -> int:
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
        # for c in 'QWER':
        #     if count[c] > n // 4:
        #         count[c] -= n // 4
        #     else:
        #         del count[c]
        #
        # start = 0
        # res = 0x3f3f3f3f
        # cur = Counter()
        # for i, c in enumerate(s):
        #     if not cur and c not in count:
        #         start += 1
        #         continue
        #
        #     cur[c] += 1
        #     if not len(count - cur):
        #         res = min(res, i - start + 1)
        #
        #         while len(count - cur) >= 0:
        #             start += 1
        #             print(s[start: i+1])
        #             cur = Counter(s[start: i+1])


def test_balanced_string():
    solution = Solution()

    assert solution.balancedString("WQWRQQQW") == 3, 'wrong result'
    assert solution.balancedString('QWER') == 0, 'wrong result'
    assert solution.balancedString('QQWE') == 1, 'wrong result'
    assert solution.balancedString('QQQW') == 2, 'wrong result'
    assert solution.balancedString('QQQQ') == 3, 'wrong result'


if __name__ == '__main__':
    test_balanced_string()
