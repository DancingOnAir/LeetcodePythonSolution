from typing import List
from math import log10
from collections import defaultdict
from itertools import combinations


class Solution:
    def countPairs(self, nums: List[int]) -> int:
        mx = int(log10(max(nums))) + 1
        strs = map(lambda x: str(x).rjust(mx, '0'), nums)

        m, res = defaultdict(list), 0
        for s in strs:
            m[''.join(sorted(s))].append(s)

        for k in m:
            for s1, s2 in combinations(m[k], 2):
                if sum(c1 != c2 for c1, c2 in zip(s1, s2)) < 3:
                    res += 1
        return res


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs([3, 12, 30, 17, 21]) == 2, 'wrong result'
    assert solution.countPairs([1, 1, 1, 1, 1]) == 10, 'wrong result'
    assert solution.countPairs([123, 231]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()
