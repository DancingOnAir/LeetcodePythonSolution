from typing import List
from itertools import accumulate
from collections import deque


class Solution:
    # mono deque to find max value in a sliding window
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        dq = deque()
        cur = i = 0
        for j in range(n):
            cur += runningCosts[j]
            # 注意等于也要pop，更新dq中的idx
            while dq and chargeTimes[dq[-1]] <= chargeTimes[j]:
                dq.pop()
            dq.append(j)
            # 这里是if 不是while
            if chargeTimes[dq[0]] + (j - i + 1) * cur > budget:
                if dq[0] == i:
                    dq.popleft()
                cur -= runningCosts[i]
                i += 1
        # 因为上面是if，所以当得到一个window的size = x，不用检查长度在x以下的子数组，这里x就是最大值，那么自然i就是最小
        return n - i

    # TLE, sliding window
    def maximumRobots1(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        l = 0
        res = 0
        pre_sum = list(accumulate(runningCosts, initial=0))
        for r in range(n):
            while max(chargeTimes[l: r + 1], default=0) + (pre_sum[r+1] - pre_sum[l]) * (r - l + 1) > budget:
                l += 1
            res = max(res, r - l + 1)
        return res


def test_maximum_robots():
    solution = Solution()
    assert solution.maximumRobots([3, 6, 1, 3, 4], [2, 1, 3, 4, 5], 25) == 3, 'wrong result'
    assert solution.maximumRobots([11, 12, 19], [10, 8, 7], 19) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_robots()
