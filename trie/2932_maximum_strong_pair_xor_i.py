from typing import List


class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        l = 0
        for r in range(len(nums)):
            while nums[r] > nums[l] * 2:
                l += 1

            for i in range(l, r+1):
                res = max(res, nums[i] ^ nums[r])
        return res


def test_maximum_strong_pair_xor():
    solution = Solution()
    assert solution.maximumStrongPairXor([1, 2, 3, 4, 5]) == 7, 'wrong result'
    assert solution.maximumStrongPairXor([10, 100]) == 0, 'wrong result'


if __name__ == '__main__':
    test_maximum_strong_pair_xor()
