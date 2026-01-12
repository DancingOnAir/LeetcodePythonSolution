from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        left, right, res = 0, 0, 0
        while right < len(nums) - 1:
            res += 1
            max_right = max(i + nums[i] for i in range(left, right + 1))
            left, right = right + 1, max_right
        return res

    def jump1(self, nums: List[int]) -> int:
        max_index, res, end = nums[0], 0, 0
        for i in range(len(nums) - 1):
            max_index = max(max_index, i + nums[i])
            if i == end:
                end = max_index
                res += 1

        return res


def test_jump():
    solution = Solution()

    nums1 = [2, 3, 1, 1, 4]
    print(solution.jump(nums1))
    nums2 = [0]
    print(solution.jump(nums2))


if __name__ == '__main__':
    test_jump()
