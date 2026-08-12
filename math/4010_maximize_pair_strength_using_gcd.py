from math import gcd


class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        # def gcd(a: int, b: int) -> int:
        #     return a if b == 0 else gcd(b, a % b)

        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
               res = max(res, (nums[i] * nums[j]) // (gcd(nums[i], nums[j]) ** 2))
        return res


def test_max_pair_strength():
    solution = Solution()
    assert solution.maxPairStrength([2, 3, 5]) == 15, 'wrong result'
    assert solution.maxPairStrength([4, 6, 8]) == 12, 'wrong result'
    assert solution.maxPairStrength([3, 3]) == 1, 'wrong result'


if __name__ == '__main__':
    test_max_pair_strength()
