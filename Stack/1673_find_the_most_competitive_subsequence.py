from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        stk = list()
        for i, x in enumerate(nums):
            while stk and stk[-1] > x:
                if len(stk) + n - i == k:
                    return stk + nums[i:]
                stk.pop()
            stk.append(x)

        return stk[: k]


def test_most_competitive():
    solution = Solution()
    # assert solution.mostCompetitive([3, 5, 2, 6], 2) == [2, 6], 'wrong result'
    assert solution.mostCompetitive([2, 4, 3, 3, 5, 4, 9, 6], 4) == [2, 3, 3, 4], 'wrong result'


if __name__ == '__main__':
    test_most_competitive()
