from typing import List


class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        d = [nums[0]]
        for i in range(1, n):
            d.append(nums[i] - nums[i - 1])

        for i in range(n - k + 1):
            if d[i] == 0:
                continue
            if d[i] < 0:
                return False
            d[i + k] += d[i]

        for i in range(n - k + 1, n):
            if d[i] > 0:
                return False
        return True


def test_check_array():
    solution = Solution()
    assert solution.checkArray([2, 2, 3, 1, 1, 0], 3), 'wrong result'
    assert not solution.checkArray([1, 3, 1, 1], 2), 'wrong result'


if __name__ == '__main__':
    test_check_array()
