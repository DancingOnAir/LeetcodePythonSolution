from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_index, res, end = nums[0], 0, 0
        for i in range(len(nums) - 1):
            # if max_index >= i:
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
