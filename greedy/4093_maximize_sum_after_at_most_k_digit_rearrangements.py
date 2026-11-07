class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        res = 0
        for i, x in enumerate(nums):
            res += x
            y = int(''.join(sorted(str(x), reverse=True)))
            nums[i] = y - x
        nums.sort(reverse=True)
        return res + sum(nums[: k])


def test_maximize_sum():
    solution = Solution()
    assert solution.maximizeSum([123, 45], k=1) == 366, 'wrong result'
    assert solution.maximizeSum([102, 90, 14], k=2) == 341, 'wrong result'


if __name__ == '__main__':
    test_maximize_sum()
