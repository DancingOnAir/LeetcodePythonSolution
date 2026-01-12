from typing import List
from heapq import heappop, heappush


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        total = sum(nums)
        hp = []
        for i, v in enumerate(nums):
            heappush(hp, (v, i))

        res = []
        seen = set()
        for i, (idx, k) in enumerate(queries):
            if idx not in seen:
                seen.add(idx)
                total -= nums[idx]
            while k and hp:
                cur = heappop(hp)
                if cur[1] not in seen:
                    seen.add(cur[1])
                    total -= cur[0]
                    k -= 1

            res.append(total)

        return res


def test_unmarked_sum_array():
    solution = Solution()
    assert solution.unmarkedSumArray([1, 2, 2, 1, 2, 3, 1], [[1, 2], [3, 3], [4, 2]]) == [8, 3, 0], 'wrong result'
    assert solution.unmarkedSumArray([1, 4, 2, 3], [[0, 1]]) == [7], 'wrong result'


if __name__ == '__main__':
    test_unmarked_sum_array()
