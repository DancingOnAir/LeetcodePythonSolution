from itertools import groupby


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        pre = 0
        for _, g in groupby(s):
            cur = len(list(g))
            if pre == 0:
                pre = cur
                continue

            res += min(pre, cur)
            pre = cur

        return res


def test_count_binary_substrings():
    solution = Solution()
    assert solution.countBinarySubstrings("00110011") == 6, 'wrong result'
    assert solution.countBinarySubstrings("10101") == 4, 'wrong result'


if __name__ == '__main__':
    test_count_binary_substrings()
