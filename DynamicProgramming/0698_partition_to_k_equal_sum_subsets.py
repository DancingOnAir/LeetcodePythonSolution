from typing import List
from collections import Counter


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
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
    assert solution.canPartitionKSubsets(nums1, k1), 'wrong result'


if __name__ == '__main__':
    test_can_partition_k_subsets()
