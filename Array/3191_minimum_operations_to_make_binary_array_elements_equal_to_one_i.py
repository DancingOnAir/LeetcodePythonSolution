from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i, j, n = 0, 2, len(nums)
        res = 0
        while j < n:
            if nums[i] == 0:
                res += 1
                for k in range(i, i + 3):
                    nums[k] = 1 if nums[k] == 0 else 0
            i += 1
            j += 1

        if nums[-1] == 0 or nums[-2] == 0:
            return -1
        return res


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([0, 1, 1, 1, 0, 0]) == 3, 'wrong result'
    assert solution.minOperations([0, 1, 1, 1]) == -1, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
