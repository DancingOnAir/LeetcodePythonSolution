from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
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
    # assert solution.maxCount([1, 6, 5], 5, 6) == 2, 'wrong result'
    assert solution.maxCount([1, 2, 3, 4, 5, 6, 7], 8, 1) == 0, 'wrong result'


if __name__ == '__main__':
    test_max_count()
