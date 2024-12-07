from typing import List
from heapq import heappop, heappush


class Solution:
    # 差分数组维护 + 贪心 + 最大堆维护最右边的端点
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key=lambda x: x[0])
        hp = []
        diff = [0] * (len(nums) + 1)
        sum_diff = j = 0
        for i, x in enumerate(nums):
            sum_diff += diff[i]
            while j < len(queries) and queries[j][0] <= i:
                heappush(hp, -queries[j][1])
                j += 1

            while sum_diff < x and hp and -hp[0] >= i:
                sum_diff += 1
                diff[-heappop(hp) + 1] -= 1

            if sum_diff < x:
                return -1
        return len(hp)


def test_max_removal():
    solution = Solution()
    assert solution.maxRemoval([2, 0, 2], [[0, 2], [0, 2], [1, 1]]) == 1, 'wrong result'
    assert solution.maxRemoval([1, 1, 1, 1], [[1, 3], [0, 2], [1, 3], [1, 2]]) == 2, 'wrong result'
    assert solution.maxRemoval([1, 2, 3, 4], [[0, 3]]) == -1, 'wrong result'


if __name__ == '__main__':
    test_max_removal()
