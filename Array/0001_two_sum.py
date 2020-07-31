class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                return [count[nums[i]], i]
            count[target - nums[i]] = i


def test_two_sum():
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))


if __name__ == '__main__':
    test_two_sum()


