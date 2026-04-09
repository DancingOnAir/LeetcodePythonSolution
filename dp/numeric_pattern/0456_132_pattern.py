class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        n = len(nums)
        mn = [nums[0]]
        for i in range(1, n):
            mn.append(min(mn[-1], nums[i]))

        stk = []
        for i in range(n - 1, 0, -1):
            if nums[i] > mn[i]:
                while stk and stk[-1] <= mn[i]:
                    stk.pop()
                if stk and nums[i] > stk[-1]:
                    return True
                stk.append(nums[i])
        return False

    # TLE
    def find132pattern2(self, nums: list[int]) -> bool:
        for k in range(2, len(nums)):
            cnt1 = 0
            for j in range(k):
                if nums[j] < nums[k]:
                    # 把 j 当作 i，把 k 当作 k，现在 nums[i] < nums[k]，即 1 < 2
                    cnt1 += 1
                elif nums[j] > nums[k]:
                    # 把 j 当作 j，把 k 当作 k，现在 nums[j] > nums[k]，即 3 > 2
                    # 前面有 "1" 就构成完整的 132 模式
                    if cnt1 > 0:
                        return True
        return False

    # TLE
    def find132pattern1(self, nums: list[int]) -> bool:
        # i, j, k = 132
        n = len(nums)
        mn = [nums[0]]
        for j in range(1, n - 1):
            mn.append(min(mn[-1], nums[j]))
            for k in range(j + 1, n):
                if nums[j] > nums[k] > mn[-1]:
                    return True
        return False


def test_find_132_pattern():
    solution = Solution()
    assert not solution.find132pattern([1, 2, 3, 4]), 'wrong result'
    assert solution.find132pattern([3, 1, 4, 2]), 'wrong result'
    assert solution.find132pattern([-1, 3, 2, 0]), 'wrong result'


if __name__ == '__main__':
    test_find_132_pattern()
