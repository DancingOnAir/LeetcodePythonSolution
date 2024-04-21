from typing import List
from collections import defaultdict, Counter


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        res = 1
        arr = sorted(cnt)
        for k in arr:
            if k ** 2 > arr[-1]:
                break

            if k == 1:
                res = cnt[k]
                continue

            val, cur = k, 0
            while val in cnt:
                if cnt[val] == 1:
                    cur += 1
                    break
                cur += 2
                val *= val
            res = max(res, cur)
        return res if res % 2 else res - 1


def test_maximum_length():
    solution = Solution()
    assert solution.maximumLength(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]) == 9, 'wrong result'
    assert solution.maximumLength([14, 14, 196, 196, 38416, 38416]) == 5, 'wrong result'
    assert solution.maximumLength([5, 4, 1, 2, 2]) == 3, 'wrong result'
    assert solution.maximumLength([1, 3, 2, 4]) == 1, 'wrong result'


if __name__ == '__main__':
    test_maximum_length()
