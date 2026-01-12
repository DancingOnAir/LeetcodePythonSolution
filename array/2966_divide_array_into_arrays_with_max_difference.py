from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            res.append(nums[i: i + 3])
        return res


def test_divide_array():
    solution = Solution()
    assert solution.divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2) == [[1, 1, 3], [3, 4, 5], [7, 8, 9]], 'wrong result'
    assert solution.divideArray([1, 3, 3, 2, 7, 3], 3) == [], 'wrong result'


if __name__ == '__main__':
    test_divide_array()
