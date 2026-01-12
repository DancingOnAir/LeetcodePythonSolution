from typing import List


class Solution:
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        n = 26
        nxt_ps = [0] * (n * 2 + 1)
        pre_ps = [0] * (n * 2 + 1)
        for i in range(n * 2):
            nxt_ps[i + 1] = nxt_ps[i] + nextCost[i % 26]
            pre_ps[i + 1] = pre_ps[i] + previousCost[i % 26]

        res = 0
        for a, b in zip(s, t):
            x = ord(a) - ord('a')
            y = ord(b) - ord('a')
            res += min(nxt_ps[y + 26 if y < x else y] - nxt_ps[x], pre_ps[(x + 26 if x < y else x) + 1] - pre_ps[y + 1])
        return res


def test_shift_distance():
    solution = Solution()
    assert solution.shiftDistance("abab", "baba",
                                  [100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                  [1, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                   0]) == 2, 'wrong result'
    assert solution.shiftDistance("leet", "code",
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                                  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                   1]) == 31, 'wrong result'


if __name__ == '__main__':
    test_shift_distance()
