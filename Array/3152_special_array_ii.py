from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ps = [0] * len(nums)
        for i in range(len(nums) - 1):
            ps[i + 1] = ps[i] + (nums[i] % 2 == nums[i + 1] % 2)

        res = []
        for a, b in queries:
            res.append(ps[b] - ps[a] <= 0)
        return res


def test_is_array_special():
    solution = Solution()
    assert solution.isArraySpecial([3, 4, 1, 2, 6], [[0, 4]]) == [False], 'wrong result'
    assert solution.isArraySpecial([4, 3, 1, 6], [[0, 2], [2, 3]]) == [False, True], 'wrong result'


if __name__ == '__main__':
    test_is_array_special()
