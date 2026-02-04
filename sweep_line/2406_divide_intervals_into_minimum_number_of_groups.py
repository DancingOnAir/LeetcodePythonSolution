from typing import List


class Solution:
    # Intuition: Meeting Room problem
    # The amount of groups needed is equal to the greatest amount of overlapping intervals
    def minGroups(self, intervals: List[List[int]]) -> int:
        endpoints = list()
        for s, e in intervals:
            # 起始点，等于占据会议室，正数记录次数
            endpoints.append([s, 1])
            # 结束点+1，等于离开会议室，负数记录次数
            endpoints.append([e + 1, -1])
        res = cur = 0
        for _, diff in sorted(endpoints):
            cur += diff
            res = max(res, cur)
        return res

    # TLE
    def minGroups1(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], x[1]))
        seen = set()
        res = 0
        while len(seen) != len(intervals):
            cur = None
            for i, interval in enumerate(intervals):
                if i in seen:
                    continue

                if cur is None or cur[1] < interval[0]:
                    cur = interval
                    seen.add(i)
            res += 1
        return res


def test_min_groups():
    solution = Solution()
    assert solution.minGroups([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]) == 3, 'wrong result'
    assert solution.minGroups([[1, 3], [5, 6], [8, 10], [11, 13]]) == 1, 'wrong result'


if __name__ == '__main__':
    test_min_groups()
