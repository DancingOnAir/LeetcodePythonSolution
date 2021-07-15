from itertools import groupby


class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = [(k, len(list(g))) for k, g in groupby(s)]
        lo, hi = 0, len(cnt) - 1
        left, right = 0, len(s)
        while lo < hi:
            if cnt[lo][0] == cnt[hi][0]:
                left += cnt[lo][1]
                right -= cnt[hi][1]

                lo += 1
                hi -= 1
            else:
                break
        if lo > hi:
            return 0
        if lo == hi:
            return 1 if cnt[lo][1] == 1 else 0
        return len(s[left: right])


def test_minimum_length():
    solution = Solution()

    assert solution.minimumLength('ca') == 2, 'wrong result'
    assert solution.minimumLength('cabaabac') == 0, 'wrong result'
    assert solution.minimumLength('aabccabba') == 3, 'wrong result'


if __name__ == '__main__':
    test_minimum_length()
