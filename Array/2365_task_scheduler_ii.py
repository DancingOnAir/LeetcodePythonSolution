from typing import List
from collections import defaultdict


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        days = 0
        next_available_day = dict()

        for t in tasks:
            days = max(days + 1, next_available_day.setdefault(t, 0))
            next_available_day[t] = days + space + 1
        return days

    def taskSchedulerII1(self, tasks: List[int], space: int) -> int:
        m = defaultdict(list)
        breaks = [0] * len(tasks)

        for i, t in enumerate(tasks):
            interval = 0
            if t in m:
                pre = m[t][-1]
                gap = breaks[i-1] - breaks[pre] + (i - pre - 1)
                if gap < space:
                    interval = space - gap

            breaks[i] += interval + breaks[i - 1]
            m[t].append(i)
        return len(tasks) + breaks[-1]


def test_task_scheduler_ii():
    solution = Solution()
    assert solution.taskSchedulerII([1, 2, 1, 2, 3, 1], 3) == 9, 'wrong result'
    assert solution.taskSchedulerII([5, 8, 8, 5], 2) == 6, 'wrong result'


if __name__ == '__main__':
    test_task_scheduler_ii()
