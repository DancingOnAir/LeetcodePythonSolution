from typing import List
from functools import cmp_to_key
from collections import defaultdict


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        d = dict()
        for i, c in enumerate(s):
            if c not in d:
                d[c] = [i, i]
            else:
                d[c][1] = i
        indexes = list(d.values())

        # after expanding left & right, no more partial overlap
        def expand(l, r):
            seen = set()
            left, right = l, r
            for i in range(l, r+1):
                if s[i] not in seen:
                    seen.add(s[i])
                    left = min(left, d[s[i]][0])
                    right = max(right, d[s[i]][1])
            return left, right

        for i, [l, r] in enumerate(indexes):
            left, right = l, r
            while (left, right) != expand(left, right):
                left, right = expand(left, right)
            indexes[i] = (left, right)
        # clear duplicates
        indexes = sorted(list(set(indexes)))

        i = 1
        while i < len(indexes):
            # coz no partial overlap & no duplicates, after sorting, there are 2 situations:
            # case 1. indexes[i-1][0] < indexes[i][0] <= indexes[i][1] < indexes[i][1]
            # case 2. indexes[i - 1] is part of indexes[i]
            if indexes[i][0] > indexes[i - 1][1]:
                i += 1
            else:
                indexes.pop(i - 1)

        res = [s[l:r+1] for l, r in indexes]
        return res


def test_max_num_of_substrings():
    solution = Solution()

    assert sorted(solution.maxNumOfSubstrings('bbcacbaba')) == sorted(["bbcacbaba"]), 'wrong result'
    assert sorted(solution.maxNumOfSubstrings('adefaddaccc')) == sorted(["e", "f", "ccc"]), 'wrong result'
    assert sorted(solution.maxNumOfSubstrings('abbaccd')) == sorted(["d", "bb", "cc"]), 'wrong result'


if __name__ == '__main__':
    test_max_num_of_substrings()
