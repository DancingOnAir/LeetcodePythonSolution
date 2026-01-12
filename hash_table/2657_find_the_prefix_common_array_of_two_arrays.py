from typing import List
from collections import Counter


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt = Counter()
        res = []
        cur = 0
        for i in range(len(A)):
            cnt[A[i]] += 1
            if cnt[A[i]] == 0:
                cur += 1
            cnt[B[i]] -= 1
            if cnt[B[i]] == 0:
                cur += 1
            res.append(cur)

        return res


def test_find_the_prefix_common_array():
    solution = Solution()
    assert solution.findThePrefixCommonArray([1, 3, 2, 4], [3, 1, 2, 4]) == [0, 2, 3, 4], 'wrong result'
    assert solution.findThePrefixCommonArray([2, 3, 1], [3, 1, 2]) == [0, 1, 3], 'wrong result'


if __name__ == '__main__':
    test_find_the_prefix_common_array()
