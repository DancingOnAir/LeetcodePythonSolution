from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        # cost[i] 表示运输前面0到i - 1下标的box船需要运输的趟数，不考虑返程
        cost = [0] * (n + 1)
        for i in range(2, n + 1):
            cost[i] = cost[i - 1]
            if boxes[i - 2][0] != boxes[i - 1][0]:
                cost[i] += 1

        dp = [0] * (n + 1)
        j = k = 1
        w = 0
        for i in range(1, n + 1):
            w += boxes[i - 1][1]
            while i - j + 1 > maxBoxes or w > maxWeight:
                w -= boxes[j - 1][1]
                j += 1
            c = cost[i] - cost[j]
            dp[i] = dp[j - 1] + c + 2
            # j与前面一个箱子不同，没有造成截断，没有优化的必要
            # c == 0 最后一车的箱子全部相同，也没有优化的必要
            if c == 0 or j == 1 or boxes[j - 2][0] != boxes[j - 1][0]:
                continue
            # 向后移动到不截断为止
            if k <= j:
                k = j + 1
                while boxes[k - 1][0] == boxes[j - 2][0]:
                    k += 1
            dp[i] = min(dp[i], dp[k - 1] + (c - 1) + 2)
        return dp[-1]


def test_box_delivering():
    solution = Solution()
    assert solution.boxDelivering([[1, 1], [2, 1], [1, 1]], 2, 3, 3) == 4, 'wrong result'
    assert solution.boxDelivering([[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], 3, 3, 6) == 6, 'wrong result'
    assert solution.boxDelivering([[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], 3, 6, 7) == 6, 'wrong result'


if __name__ == '__main__':
    test_box_delivering()
