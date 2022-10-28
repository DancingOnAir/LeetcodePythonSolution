from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def gcd(a, b):
            return a if b == 0 else gcd(b, a % b)

        res = 0
        for i in range(len(nums)):
            if nums[i] % k == 0:
                if nums[i] == k:
                    res += 1

                g = nums[i]
                for j in range(i + 1, len(nums)):
                    g = gcd(g, nums[j])
                    if g % k != 0:
                        break
                    if g == k:
                        res += 1
        return res


def test_subarray_gcd():
    solution = Solution()
    assert solution.subarrayGCD([3, 12, 9, 6], 3) == 7, 'wrong result'
    assert solution.subarrayGCD([9, 3, 1, 2, 6, 3], 3) == 4, 'wrong result'
    assert solution.subarrayGCD([4], 7) == 0, 'wrong result'


if __name__ == '__main__':
    test_subarray_gcd()
