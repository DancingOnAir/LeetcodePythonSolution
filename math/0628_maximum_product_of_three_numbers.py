class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-3] * nums[-2] * nums[-1])


def test_maximum_product():
    solution = Solution()
    assert solution.maximumProduct([1,2,3]) == 6, "wrong result"
    assert solution.maximumProduct([1,2,3,4]) == 24, "wrong result"
    assert solution.maximumProduct([-1,-2,-3]) == -6, "wrong result"


if __name__ == '__main__':
    test_maximum_product()

