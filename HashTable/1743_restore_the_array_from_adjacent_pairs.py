from typing import List
from collections import Counter


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        freq = dict()
        for p in adjacentPairs:
            freq.setdefault(p[0], set()).add(p[1])
            freq.setdefault(p[1], set()).add(p[0])

        cur = 0
        for k, v in freq.items():
            if len(v) == 1:
                cur = k
                break

        res = list()
        used = set()
        while len(res) <= len(adjacentPairs):
            res.append(cur)
            used.add(cur)

            for x in freq[cur]:
                if x not in used:
                    cur = x
                    break
        return res


def test_restore_array():
    solution = Solution()

    assert solution.restoreArray([[2, 1], [3, 4], [3, 2]]) == [1, 2, 3, 4], 'wrong result'
    assert solution.restoreArray([[4, -2], [1, 4], [-3, 1]]) == [-2, 4, 1, -3], 'wrong result'


if __name__ == '__main__':
    test_restore_array()

