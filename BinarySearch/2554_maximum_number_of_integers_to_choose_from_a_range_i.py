from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    # hashset
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        res = 0
        s = set(banned)
        for i in range(1, n + 1):
            if maxSum < 0:
                break

            if i not in s:
                maxSum -= i
                res += maxSum >= 0
        return res

    # binary search
    def maxCount2(self, banned: List[int], n: int, maxSum: int) -> int:
        pre_sum = [0]
        banned = sorted(set(banned))
        for x in banned:
            pre_sum.append(x + pre_sum[-1])

        left, right, mx = 1, n, 0
        res = 0
        while left <= right:
            mid = left + (right - left) // 2
            pos = bisect_right(banned, mid)
            total = (1 + mid) * mid // 2 - pre_sum[pos]
            if total < maxSum:
                if total > mx:
                    mx = total
                    res = mid - pos

                left = mid + 1
            elif total > maxSum:
                right = mid - 1
            else:
                return mid - pos
        return res

    # two pointers
    def maxCount1(self, banned: List[int], n: int, maxSum: int) -> int:
        i = j = total = res = 0
        banned.sort()
        while i < n:
            if i + 1 < banned[j] or (i + 1 > banned[j] and j == len(banned) - 1):
                if total + i + 1 > maxSum:
                    return res
                total += i + 1
                res += 1
                i += 1
            elif i + 1 == banned[j]:
                i += 1
                if j < len(banned) - 1:
                    j += 1
            else:
                if j < len(banned) - 1:
                    j += 1
        return res


def test_max_count():
    solution = Solution()
    assert solution.maxCount([11], 7, 50) == 7, 'wrong result'
    assert solution.maxCount([1, 6, 5], 5, 6) == 2, 'wrong result'
    assert solution.maxCount([1, 2, 3, 4, 5, 6, 7], 8, 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_count()
