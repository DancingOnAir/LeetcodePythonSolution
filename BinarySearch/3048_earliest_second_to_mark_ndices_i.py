from typing import List


class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def check(time):
            arr = [-1] * n
            for i, v in enumerate(changeIndices[:time]):
                arr[v - 1] = i
            if -1 in arr:
                return False

            cnt = 0
            for i, v in enumerate(changeIndices[:time]):
                v -= 1
                if arr[v] == i:
                    if nums[v] > cnt:
                        return False
                    cnt -= nums[v]
                else:
                    cnt += 1
            return True

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
    assert solution.earliestSecondToMarkIndices([2, 2, 0], [2, 2, 2, 2, 3, 2, 2, 1]) == 8, 'wrong result'
    assert solution.earliestSecondToMarkIndices([1, 3], [1, 1, 1, 2, 1, 1, 1]) == 6, 'wrong result'
    assert solution.earliestSecondToMarkIndices([0, 1], [2, 2, 2]) == -1, 'wrong result'


if __name__ == '__main__':
    test_earliest_second_to_mark_indices()
