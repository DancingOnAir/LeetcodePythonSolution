class Solution:
    def check(self, nums: list[int]) -> bool:
        return sum(nums[i - 1] > nums[i] for i in range(len(nums))) < 2

    def check2(self, nums: list[int]) -> bool:
        cnt = 0
        n = len(nums)
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                cnt += 1
        return cnt < 2

    def check1(self, nums: list[int]) -> bool:
        decease = False
        n = len(nums)
        for i in range(n):
            if i == n - 1:
                if decease and nums[i] > nums[0]:
                    return False
            elif nums[i] > nums[i + 1]:
                if decease:
                    return False
                decease = True
        return True


def test_check():
    solution = Solution()
    assert solution.check([3, 4, 5, 1, 2]), 'wrong result'
    assert not solution.check([2, 1, 3, 4]), 'wrong result'
    assert solution.check([1, 2, 3]), 'wrong result'


if __name__ == '__main__':
    test_check()
