from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        mp = {x: i for i, x in enumerate(removable)}

        def is_subsequence(x):
            k = 0
            for i, c in enumerate(s):
                # if this c is in the range [0, x), then skip it
                if mp.get(i, float('inf')) < x:
                    continue
                if k < len(p) and c == p[k]:
                    k += 1
            return k == len(p)

        lo, hi = -1, len(removable)
        while lo < hi:
            mid = lo + hi + 1 >> 1
            if is_subsequence(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo


def test_maximum_removals():
    solution = Solution()
    assert solution.maximumRemovals('abcacb', 'ab', [3, 1, 0]) == 2, 'wrong result'
    assert solution.maximumRemovals('abcbddddd', 'abcd', [3, 2, 1, 4, 5, 6]) == 1, 'wrong result'
    assert solution.maximumRemovals('abcab', 'abc', [0, 1, 2, 3, 4]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_removals()
