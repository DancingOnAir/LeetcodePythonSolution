class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        count = {}
        for i, v in enumerate(nums):
            if v in count:
                return [count[v], i]
            count[target - v] = i
        return []

    def twoSum1(self, nums: list, target: int) -> list:
        count = {}
        for i in range(len(nums)):
            if nums[i] in count:
                return [count[nums[i]], i]
            count[target - nums[i]] = i
        return []


def test_two_sum():
    solution = Solution()

    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum(nums, target))


if __name__ == '__main__':
    test_two_sum()


