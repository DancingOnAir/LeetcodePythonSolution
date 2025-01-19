from typing import List


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        res = 1
        nums.sort()
        pre = nums[0] - k
        for x in nums[1:]:
            if pre < x + k:
                if x - k > pre:
                    pre = x - k
                elif x - k <= pre:
                    pre += 1
                res += 1
        return res


def test_max_distinct_elements():
    solution = Solution()
    assert solution.maxDistinctElements([1, 2, 2, 3, 3, 4], 2) == 6, 'wrong result'
    assert solution.maxDistinctElements([4, 4, 4, 4], 1) == 3, 'wrong result'


if __name__ == '__main__':
    test_max_distinct_elements()
