from typing import List


class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        res = sum(abs(a - b) for a, b in zip(arr, brr))
        if res <= k:
            return res
        return min(res, sum(abs(a - b) for a, b in zip(sorted(arr), sorted(brr))) + k)


def test_min_cost():
    solution = Solution()
    assert solution.minCost([-7, 9, 5], [7, -2, -5], 2) == 13, 'wrong result'
    assert solution.minCost([2, 1], [2, 1], 0) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_cost()
