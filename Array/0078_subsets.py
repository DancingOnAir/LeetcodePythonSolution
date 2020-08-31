from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
