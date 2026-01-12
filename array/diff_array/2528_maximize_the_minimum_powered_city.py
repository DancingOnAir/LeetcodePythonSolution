from typing import List
from itertools import accumulate


class Solution:
    # https://leetcode.cn/problems/maximize-the-minimum-powered-city/solutions/2050272/er-fen-da-an-qian-zhui-he-chai-fen-shu-z-jnyv/
    # 看到「最大化最小值」或者「最小化最大值」就要想到二分, 这是一个固定的套路。
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        pre_sum = list(accumulate(stations, initial=0))

        for i in range(n):
            stations[i] = pre_sum[min(n, i + r + 1)] - pre_sum[max(0, i - r)]

        def check(x):
            diff = [0] * n
            sum_diff = need = 0
            for i, power in enumerate(stations):
                sum_diff += diff[i]
                m = x - power - sum_diff
                if m > 0:
                    need += m
                    if need > k:
                        return False
                    sum_diff += m
                if i + 2 * r + 1 < n:
                    diff[i + 2 * r + 1] -= m
            return True

        left = min(stations)
        right = left + k + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left


def test_max_power():
    solution = Solution()
    assert solution.maxPower([1, 2, 4, 5, 0], 1, 2) == 5, 'wrong result'
    assert solution.maxPower([4, 4, 4, 4], 0, 3) == 4, 'wrong result'


if __name__ == '__main__':
    test_max_power()
