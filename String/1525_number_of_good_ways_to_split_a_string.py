from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        cur, total = set(), Counter(s)
        res, cnt = 0, len(total)

        for i, c in enumerate(s):
            cur.add(c)
            total[c] -= 1

            cnt -= not total[c]
            res += len(cur) == cnt

        return res

    def numSplits2(self, s: str) -> int:
        c1 = Counter()
        c2 = Counter(s)
        res = 0

        for c in s:
            c1[c] += 1
            c2[c] -= 1

            if not c2[c]:
                del c2[c]

            if len(c1) == len(c2):
                res += 1
        return res

    def numSplits1(self, s: str) -> int:
        def helper(c):
            return sum(1 if i > 0 else 0 for i in c)

        c1, c2 = [0] * 26, [0] * 26
        for c in s:
            c1[ord(c) - 97] += 1

        res = 0
        for c in s:
            idx = ord(c) - 97
            c1[idx] -= 1
            c2[idx] += 1

            if helper(c1) == helper(c2):
                res += 1

        return res


def test_num_splits():
    solution = Solution()
    assert solution.numSplits('aacaba') == 2, 'wrong result'
    assert solution.numSplits('abcd') == 1, 'wrong result'
    assert solution.numSplits('aaaaa') == 4, 'wrong result'
    assert solution.numSplits('acbadbaada') == 2, 'wrong result'


if __name__ == '__main__':
    test_num_splits()
