from typing import List


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        res = nums.pop()
        while nums:
            if nums[-1] <= res:
                res += nums.pop()
            else:
                # 这里因为nums[-1] > res, 可以直接替换掉之前的值, 让res=nums[-1]
                res = nums.pop()
        return res

    def maxArrayValue1(self, nums: List[int]) -> int:
        res = []
        cur = nums.pop()
        while nums:
            if nums[-1] <= cur:
                cur += nums.pop()
            else:
                res.append(cur)
                cur = nums.pop()

        res.append(cur)
        return max(res)


def test_max_array_value():
    solution = Solution()
    assert solution.maxArrayValue([2, 3, 7, 9, 3]) == 21, 'wrong result'
    assert solution.maxArrayValue([5, 3, 3]) == 11, 'wrong result'


if __name__ == '__main__':
    test_max_array_value()
