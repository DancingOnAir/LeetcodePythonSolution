class Solution:
    def countConsistent(self, nums: list[int]) -> int:
        n = len(nums)
        # -1 是哨兵
        stk = [-1]
        left = [0] * n
        for i, x in enumerate(nums):
            # x 是最小值
            while len(stk) > 1 and (nums[stk[-1]] & x) == x:
                stk.pop()
            # nums[left[i]] 不是 x 的子集
            left[i] = stk[-1]
            stk.append(i)

        stk = [n]
        res = 0
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while len(stk) > 1 and nums[stk[-1]] != x and (nums[stk[-1]] & x) == x:
                stk.pop()
            right = stk[-1]
            stk.append(i)

            res += (i - left[i]) * (right - i)
        return res


def test_count_consistent():
    solution = Solution()
    assert solution.countConsistent([5, 3, 1, 2]) == 6, 'wrong result'
    assert solution.countConsistent([1, 1, 1]) == 6, 'wrong result'
    assert solution.countConsistent([0]) == 1, 'wrong result'


if __name__ == '__main__':
    test_count_consistent()
