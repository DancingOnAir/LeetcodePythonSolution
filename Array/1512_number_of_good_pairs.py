from typing import List
from collections import Counter


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for key in count:
            if count[key] > 1:
                res += count[key] * (count[key] - 1) // 2
        return res


def test_num_identical_pairs():
    solution = Solution()

    nums1 = [1, 2, 3, 1, 1, 3]
    print(solution.numIdenticalPairs(nums1))

    nums2 = [1, 1, 1, 1]
    print(solution.numIdenticalPairs(nums2))

    nums3 = [1, 2, 3]
    print(solution.numIdenticalPairs(nums3))


if __name__ == '__main__':
    test_num_identical_pairs()
