from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for i in range(1, len(nums)):
            res &= set(nums[i])
        return sorted(res)


def test_intersection():
    solution = Solution()
    assert solution.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]) == [3, 4], 'wrong result'
    assert solution.intersection([[1, 2, 3], [4, 5, 6]]) == [], 'wrong result'


if __name__ == '__main__':
    test_intersection()
