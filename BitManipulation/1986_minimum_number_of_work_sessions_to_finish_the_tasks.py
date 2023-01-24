from typing import List
from functools import lru_cache


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)
        dp = [n] * (1 << n)
        # 预处理每个状态
        for i in range(1, 1 << n):
            j = i
            idx = 0
            consuming = 0
            while j > 0:
                bit = j & 1
                if bit:
                    consuming += tasks[idx]
                j >>= 1
                idx += 1

            if consuming <= sessionTime:
                dp[i] = 1

        for i in range(1, 1 << n):
            if dp[i] == 1:
                continue
            # 由于转移是由子集和补集得来，因此可以将子集分割为2块，避免重复枚举
            split = i >> 1
            j = i
            while j > split:
                dp[i] = min(dp[i], dp[j] + dp[j ^ i])
                j = (j - 1) & i

        return dp[(1 << n) - 1]

    # https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/solutions/1431829/python-dynamic-programming-on-subsets-explained/
    def minSessions1(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        # output: session number, consuming time
        @lru_cache(None)
        def dp(mask):
            # always have one session waiting for tasks, let me give some examples for pieces and last
            # pieces = 3, last =1 : Meaning there are three sessions, and the lastest one is accumulated with 1 unit time task. Like this: [x, y, 1], x y stands for the 1st and 2nd session, both can't take any more task.
            # pieces = 1, last = 2. Meaning there are one session, which accumulated with 2 units time tasks. Like this [2]
            # So, for all 0s, you still have one session pending for tasks to fill, but this session is currently empty, like this [0]. That's why you will have 1 session as your initial state
            if not mask:
                return 1, 0

            res = (n, sessionTime)
            for i in range(n):
                if mask & (1 << i):
                    session_num, consuming_time = dp(mask - (1 << i))
                    if consuming_time + tasks[i] > sessionTime:
                        res = min(res, (session_num + 1, tasks[i]))
                    else:
                        res = min(res, (session_num, consuming_time + tasks[i]))
            return res
        return dp((1 << n) - 1)[0]


def test_min_sessions():
    solution = Solution()
    assert solution.minSessions([1, 2, 3], 3) == 2, 'wrong result'
    assert solution.minSessions([3, 1, 3, 1, 1], 8) == 2, 'wrong result'
    assert solution.minSessions([1, 2, 3, 4, 5], 15) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_sessions()
