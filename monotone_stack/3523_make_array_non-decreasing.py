from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stk = []
        for x in nums:
            if not stk or x >= stk[-1]:
                stk.append(x)
        return len(stk)


def test_maximum_possible_size():
    solution = Solution()
    assert solution.maximumPossibleSize([4, 2, 5, 3, 5]) == 3, 'wrong result'
    assert solution.maximumPossibleSize([1, 2, 3]) == 3, 'wrong result'


if __name__ == '__main__':
    test_maximum_possible_size()
