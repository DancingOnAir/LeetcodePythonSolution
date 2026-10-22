class Solution:
    def resilientSubarray(self, nums: list[int], k: int) -> int:
        res = cnt = 0
        for i, x in enumerate(nums):
            r = x % k
            if i > 0 and nums[i - 1] % k == r:
                cnt += 1
            else:
                cnt = 1

            if (cnt - 1) * r % k == 0:
                res = max(res, cnt)
        return res


def test_resilient_subarray():
    solution = Solution()
    assert solution.resilientSubarray([2,4,6,3], k = 2) == 3, 'wrong result'
    assert solution.resilientSubarray([1,4,7,1], k = 3) == 4, 'wrong result'
    assert solution.resilientSubarray([5,5,4,8], k = 4) == 2, 'wrong result'


if __name__ == '__main__':
    test_resilient_subarray()

