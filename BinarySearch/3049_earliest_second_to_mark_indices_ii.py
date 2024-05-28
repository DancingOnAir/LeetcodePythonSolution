from typing import List
from heapq import heappush, heappop


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        first = {}
        for i, v in enumerate(changeIndices):
            if nums[v - 1] and v not in first:
                first[v] = i

        first_inv = {i: v for v, i in first.items()}

        def check(time):
            hp = []
            cnt = 0
            for i in range(time - 1, -1, -1):
                if i in first_inv:
                    heappush(hp, nums[first_inv[i] - 1])
                    if cnt > 0:
                        cnt -= 1
                    else:
                        cnt += 1
                        heappop(hp)
                else:
                    cnt += 1
            return sum(nums) + len(nums) - sum(hp) - len(hp) <= cnt

        n, m = len(nums), len(changeIndices)
        l, r = 1, m
        while l <= r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l if l <= m else -1


def test_earliest_second_to_mark_indices():
    solution = Solution()
    assert solution.earliestSecondToMarkIndices([3, 2, 3], [1, 3, 2, 2, 2, 2, 3]) == 6, 'wrong result'
    assert solution.earliestSecondToMarkIndices([0, 0, 1, 2], [1, 2, 1, 2, 1, 2, 1, 2]) == 7, 'wrong result'
    assert solution.earliestSecondToMarkIndices([1, 2, 3], [1, 2, 3]) == -1, 'wrong result'


if __name__ == '__main__':
    test_earliest_second_to_mark_indices()
