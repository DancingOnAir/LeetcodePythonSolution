from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res

    def createTargetArray1(self, nums: List[int], index: List[int]) -> List[int]:
        for i, val in enumerate(index):
            for j in range(len(index[:i])):
                if val <= index[j]:
                    index[j] += 1
        res = [0] * len(nums)
        for i in range(len(res)):
            res[index[i]] = nums[i]

        return res


def test_create_target_array():
    solution = Solution()

    nums1 = [0, 1, 2, 3, 4]
    index1 = [0, 1, 2, 2, 1]
    print(solution.createTargetArray(nums1, index1))

    nums2 = [1, 2, 3, 4, 0]
    index2 = [0, 1, 2, 3, 0]
    print(solution.createTargetArray(nums2, index2))

    nums3 = [1]
    index3 = [0]
    print(solution.createTargetArray(nums3, index3))


if __name__ == '__main__':
    test_create_target_array()
