from typing import List
from bisect import bisect_left


class Solution:
    # binary search
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # leetcode 240: search a 2d matrix II,找到不大于x的元素有多少个
        def count_less_or_equal(x):
            cnt = 0
            c = n - 1
            for r in range(n):
                while c >= 0 and matrix[r][c] > x:
                    c -= 1
                cnt += c + 1
            return cnt

        n = len(matrix)
        l, r = matrix[0][0], matrix[-1][-1]
        res = -1
        while l <= r:
            mid = l + (r - l) // 2
            if count_less_or_equal(mid) >= k:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res

    # brute force
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        arr = list()
        for r in matrix:
            arr += r
        return sorted(arr)[k - 1]


def test_kth_smallest():
    solution = Solution()
    assert solution.kthSmallest([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 3) == 5, 'wrong result'
    assert solution.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13, 'wrong result'
    assert solution.kthSmallest([[-5]], 1) == -5, 'wrong result'


if __name__ == '__main__':
    test_kth_smallest()
