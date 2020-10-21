from typing import List


class Solution:
    # brute force
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MODULO = 10 ** 9 + 7
        sums = list()

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                sums.append(total)

        sums.sort()
        res = sum(sums[left - 1: right]) % MODULO
        return res

    def rangeSum1(self, nums: List[int], n: int, left: int, right: int) -> int:
        presum = [0]
        for num in nums:
            presum.append(presum[-1] + num)

        subarrays = nums + presum[2:]
        for i in range(1, len(presum)):
            for j in range(2, len(nums)):
                if i + j <= len(nums):
                    subarrays.append(presum[i + j] - presum[i])
        subarrays.sort()
        return sum(subarrays[left - 1: right]) % 1000000007


def test_range_sum():
    solution = Solution()

    nums1 = [1, 2, 3, 4]
    n1 = 4
    left1 = 1
    right1 = 5
    print(solution.rangeSum(nums1, n1, left1, right1))

    nums2 = [1, 2, 3, 4]
    n2 = 4
    left2 = 1
    right2 = 10
    print(solution.rangeSum(nums2, n2, left2, right2))


if __name__ == '__main__':
    test_range_sum()
