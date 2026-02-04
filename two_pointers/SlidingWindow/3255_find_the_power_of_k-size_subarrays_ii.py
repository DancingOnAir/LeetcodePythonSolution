from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []
        cnt = 0
        for i, x in enumerate(nums):
            if i == 0 or x == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 1

            res.append(x if cnt >= k else -1)
        return res[k - 1:]

    def resultsArray1(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * (len(nums) - k + 1)
        cnt = 0
        for i, x in enumerate(nums):
            if i == 0 or x == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 1

            if cnt >= k:
                res[i - k + 1] = x

        return res


def test_results_array():
    solution = Solution()
    assert solution.resultsArray([1, 3, 4], 2) == [-1, 4], 'wrong result'
    assert solution.resultsArray([1, 2, 3, 4, 3, 2, 5], 3) == [3, 4, -1, -1, -1], 'wrong result'
    assert solution.resultsArray([2, 2, 2, 2, 2], 4) == [-1, -1], 'wrong result'
    assert solution.resultsArray([3, 2, 3, 2, 3, 2], 2) == [-1, 3, -1, 3, -1], 'wrong result'


if __name__ == '__main__':
    test_results_array()
