from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        res = 0
        while len(nums) > 1:
            a = heappop(nums)
            if a >= k:
                break

            res += 1
            b = heappop(nums)
            heappush(nums, a * 2 + b)

        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([2, 11, 10, 1, 3], 10) == 2, 'wrong result'
    assert solution.minOperations([1, 1, 2, 4, 9], 20) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
