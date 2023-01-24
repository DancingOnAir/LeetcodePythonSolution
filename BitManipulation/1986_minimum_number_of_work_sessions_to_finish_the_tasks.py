from typing import List
from functools import lru_cache


class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        # output: session number, consuming time
        @lru_cache(None)
        def dp(mask):
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
