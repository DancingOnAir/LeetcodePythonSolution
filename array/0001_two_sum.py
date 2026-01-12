class Solution:
    # two pointers
    def twoSum(self, nums: list, target: int) -> list:
        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x: x[1])
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l][1] + nums[r][1] == target:
                return [nums[l][0], nums[r][0]]
            elif nums[l][1] + nums[r][1] < target:
                l += 1
            else:
                r -= 1

    # hash table with enumerate
    def twoSum1(self, nums: list, target: int) -> list:
        count = {}
        for i, v in enumerate(nums):
            if v in count:
                return [count[v], i]
            count[target - v] = i
        return []

    # hash table
    def twoSum2(self, nums: list, target: int) -> list:
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
