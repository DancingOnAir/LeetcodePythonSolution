from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # 预计算间隔的空闲时间，注意是start[i + 1] - end[i]
        free = [startTime[0]] + [s - e for s, e in zip(startTime[1:], endTime)] + [eventTime - endTime[-1]]
        res = tot = 0
        for i, f in enumerate(free):
            tot += f
            if i < k:
                continue
            res = max(res, tot)
            tot -= free[i - k]
        return res


def test_max_free_time():
    solution = Solution()
    assert solution.maxFreeTime(5, k=1, startTime=[1, 3], endTime=[2, 5]) == 2, 'wrong result'
    assert solution.maxFreeTime(10, k=1, startTime=[0, 2, 9], endTime=[1, 4, 10]) == 6, 'wrong result'
    assert solution.maxFreeTime(5, k=2, startTime=[0, 1, 2, 3, 4], endTime=[1, 2, 3, 4, 5]) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_free_time()
