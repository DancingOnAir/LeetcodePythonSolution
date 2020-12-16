from typing import List


class Solution:
    # top to down dp
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, remainder = divmod(sum(nums), k)
        if remainder or max(nums) > target:
            return False

        memo = [None] * (1 << len(nums))
        memo[-1] = True

        def search(used, todo):
            if memo[used] is None:
                tar = (todo - 1) % target + 1
                memo[used] = any(search(used | (1 << i), todo - num) for i, num in enumerate(nums) if (not ((used >> i) & 1)) and num <= tar)
            return memo[used]

        return search(0, target * k)

    # down to top dp
    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        target, remainder = divmod(sum(nums), k)
        if remainder:
            return False

        if 1 == k:
            return True

        n = len(nums)
        m = 1 << n
        dp = [0] + [-1] * (m - 1)
        for mask in range(m):
            if dp[mask] == -1:
                continue

            for i in range(n):
                if not (mask & (1 << i)) and dp[mask] + nums[i] <= target:
                    dp[mask + (1 << i)] = (dp[mask] + nums[i]) % target

        return dp[m - 1] == 0

    # backtracking
    def canPartitionKSubsets1(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True

        target, remainder = divmod(sum(nums), k)
        if remainder:
            return False

        def search(groups):
            if not nums:
                return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups):
                        return True
                    groups[i] -= v
                if not group:
                    break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target:
            return False

        while nums and nums[-1] == target:
            k -= 1
            nums.pop()

        return search([0] * k)


def test_can_partition_k_subsets():
    solution = Solution()

    nums1 = [4, 3, 2, 3, 5, 2, 1]
    k1 = 4
    # assert solution.canPartitionKSubsets(nums1, k1), 'wrong result'

    nums2 = [2, 2, 3, 2]
    k2 = 3
    assert not solution.canPartitionKSubsets(nums2, k2), 'wrong result'


if __name__ == '__main__':
    test_can_partition_k_subsets()
