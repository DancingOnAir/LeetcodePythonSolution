from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res = 0
        stk = []
        for x in nums:
            while stk and x < stk[-1]:
                stk.pop()
                res += 1
            if not stk or stk[-1] != x:
                stk.append(x)
        return res + len(stk) - (stk[0] == 0)


def test_min_operations():
    solution = Solution()
    assert solution.minOperations([0, 2]) == 1, 'wrong result'
    assert solution.minOperations([3, 1, 2, 1]) == 3, 'wrong result'
    assert solution.minOperations([1, 2, 1, 2, 1, 2]) == 4, 'wrong result'


if __name__ == '__main__':
    test_min_operations()
