from typing import List
from bisect import bisect_left


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left = [0] * n
        cnt = [0] * 2
        ps = [0] * (n + 1)
        l = 0
        for i, c in enumerate(s):
            cnt[ord(c) & 1] += 1
            while cnt[0] > k and cnt[1] > k:
                cnt[ord(s[l]) & 1] -= 1
                l += 1
            left[i] = l
            ps[i + 1] = ps[i] + i - l + 1

        res = []
        for l, r in queries:
            j = bisect_left(left, l, l, r + 1)
            res.append(ps[r + 1] - ps[j] + (j - l + 1) * (j - l) // 2)
        return res


def test_count_k_constraint_substrings():
    solution = Solution()
    assert solution.countKConstraintSubstrings("0001111", 2, [[0, 6]]) == [26], 'wrong result'
    assert solution.countKConstraintSubstrings("010101", 1, [[0, 5], [1, 4], [2, 3]]) == [15, 9, 3], 'wrong result'


if __name__ == '__main__':
    test_count_k_constraint_substrings()
