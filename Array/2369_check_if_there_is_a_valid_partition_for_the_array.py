from typing import List


class Solution:
    # TLE
    def validPartition(self, nums: List[int]) -> bool:
        def valid(arr):
            n = len(arr)
            if n == 2 and arr[0] == arr[1]:
                return True
            elif n == 3 and (arr[0] == arr[1] == arr[2] or arr[0] + 2 == arr[1] + 1 == arr[2]):
                return True
            return False

        n = len(nums)
        if n < 2:
            return False
        if n == 2 or n == 3:
            return valid(nums)
        return (valid(nums[:2]) and self.validPartition(nums[2:])) or  (valid(nums[:3]) and self.validPartition(nums[3:]))


def test_valid_partition():
    solution = Solution()
    assert not solution.validPartition([993335,993336,993337,993338,993339,993340,993341]), 'wrong result'
    assert solution.validPartition([4, 4, 4, 5, 6]), 'wrong result'
    assert not solution.validPartition([1, 1, 1, 2]), 'wrong result'


if __name__ == '__main__':
    test_valid_partition()
