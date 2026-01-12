from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        hp = []
        for x in nums[1:]:
            heappush(hp, x)
        return nums[0] + heappop(hp) + heappop(hp)

    def minimumCost1(self, nums: List[int]) -> int:
        return nums[0] + sum(sorted(nums[1:])[:2])


def test_minimum_cost():
    solution = Solution()
    assert solution.minimumCost([1,2,3,12]) == 6, 'wrong result'
    assert solution.minimumCost([5,4,3]) == 12, 'wrong result'
    assert solution.minimumCost([10,3,1,1]) == 12, 'wrong result'


if __name__ == '__main__':
    test_minimum_cost()
