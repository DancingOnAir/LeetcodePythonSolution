class Solution:
    # exception
    def removeElement(self, nums: list, val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break

        return len(nums)

    # list comprehension
    def removeElement1(self, nums: list, val: int) -> int:
        nums[:] = [i for i in nums if i != val]
        return len(nums)

    # enumerate
    def removeElement2(self, nums: list, val: int) -> int:
        res = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[i], nums[res] = nums[res], nums[i]
                res += 1
        nums = nums[: res]
        return res

    def removeElement3(self, nums: list, val: int) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1
        return res


def test_remove_element():
    solution = Solution()

    nums1 = [3, 2, 2, 3]
    val1 = 3
    print(solution.removeElement(nums1, val1))
    print(nums1)

    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print(solution.removeElement(nums2, val2))
    print(nums2)
    pass


if __name__ == '__main__':
    test_remove_element()