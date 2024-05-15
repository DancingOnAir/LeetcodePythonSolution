from typing import List
from heapq import heapify, heappop


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 2):
            res.append(nums[i + 1])
            res.append(nums[i])
        return res

    def numberGame1(self, nums: List[int]) -> List[int]:
        res = []
        heapify(nums)
        while nums:
            cur = []
            for _ in range(2):
                cur.append(heappop(nums))
            res += cur[::-1]
        return res


def test_number_game():
    solution = Solution()
    assert solution.numberGame([5, 4, 2, 3]) == [3, 2, 5, 4], 'wrong result'
    assert solution.numberGame([2, 5]) == [5, 2], 'wrong result'


if __name__ == '__main__':
    test_number_game()
