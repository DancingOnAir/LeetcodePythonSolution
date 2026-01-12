from typing import List
from itertools import combinations


class Solution:
    # bit mask solution
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [[nums[i] for i in range(len(nums)) if mask >> i & 1]
                for mask in range(2 ** len(nums))]

    # itertool lib solution
    def subsets3(self, nums: List[int]) -> List[List[int]]:
        return [list(s) for n in range(len(nums) + 1) for s in combinations(nums, n)]

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [i + [num] for i in res]
        return res

    def subsets1(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        def backtracking(path, level):
            res.append(path[:])
            for i in range(level, len(nums)):
                path.append(nums[i])
                backtracking(path, i + 1)
                path.pop()

        res = []
        backtracking([], 0)

        return res


def test_subsets():
    solution = Solution()

    nums1 = [1, 2, 3]
    print(solution.subsets(nums1))

    nums2 = [0]
    print(solution.subsets(nums2))


if __name__ == '__main__':
    test_subsets()
