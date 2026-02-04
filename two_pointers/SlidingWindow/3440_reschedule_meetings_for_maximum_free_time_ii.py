from typing import List


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        def get(i):
            if i == 0:
                return startTime[0]
            if i == n:
                return eventTime - endTime[-1]
            return startTime[i] - endTime[i - 1]

        max_a, max_b, max_c = 0, -1, -1
        for i in range(1, n + 1):
            sz = get(i)
            if sz > get(max_a):
                max_a, max_b, max_c = i, max_a, max_b
            elif max_b < 0 or sz > get(max_b):
                max_b, max_c = i, max_b
            elif max_c < 0 or sz > get(max_c):
                max_c = i

        res = 0
        for i, (s, e) in enumerate(zip(startTime, endTime)):
            sz = e - s
            if i != max_a and i + 1 != max_a and sz <= get(max_a) or i != max_b and i + 1 != max_b and sz <= get(max_b) or sz <= get(max_c):
                res = max(res, get(i) + sz + get(i + 1))
            else:
                res = max(res, get(i) + get(i + 1))
        return res


def test_max_free_time():
    solution = Solution()
    assert solution.maxFreeTime(5, startTime=[1, 3], endTime=[2, 5]) == 2, 'wrong result'
    assert solution.maxFreeTime(10, startTime = [0,7,9], endTime = [1,8,10]) == 7, 'wrong result'
    assert solution.maxFreeTime(10, startTime = [0,3,7,9], endTime = [1,4,8,10]) == 6, 'wrong result'


if __name__ == '__main__':
    test_max_free_time()
