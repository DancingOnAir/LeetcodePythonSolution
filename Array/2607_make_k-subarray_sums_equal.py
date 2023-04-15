from typing import List
from math import gcd


class Solution:
    # bedzout's lamma + greedy
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        k = gcd(k, n)
        res = 0
        for i in range(k):
            b = sorted(arr[i::k])
            mid = b[len(b) // 2]
            res += sum(abs(mid - x) for x in b)

        return res


def test_make_sub_k_equal():
    solution = Solution()
    assert solution.makeSubKSumEqual([1, 4, 1, 3], 2) == 1, 'wrong result'
    assert solution.makeSubKSumEqual([2, 5, 5, 7], 3) == 5, 'wrong result'


if __name__ == '__main__':
    test_make_sub_k_equal()

