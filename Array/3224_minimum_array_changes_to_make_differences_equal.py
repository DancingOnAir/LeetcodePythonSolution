from typing import List
from collections import Counter


class Solution:
    # https://leetcode.cn/problems/minimum-array-changes-to-make-differences-equal/solutions/2851502/mei-ju-x-fen-lei-tao-lun-pythonjavacgo-b-puh2/
    def minChanges(self, nums: List[int], k: int) -> int:
        cnt1 = [0] * (k + 1)
        cnt2 = [0] * (k + 1)
        n = len(nums)
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            if a > b:
                a, b = b, a
            cnt1[b - a] += 1
            cnt2[max(b, k - a)] += 1

        res = n
        total = 0
        for c1, c2 in zip(cnt1, cnt2):
            res = min(res, n // 2 - c1 + total)
            total += c2
        return res


def test_min_changes():
    solution = Solution()
    assert solution.minChanges([1, 0, 1, 2, 4, 3], 4) == 2, 'wrong result'
    assert solution.minChanges([0, 1, 2, 3, 3, 6, 5, 4], 6) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_changes()

