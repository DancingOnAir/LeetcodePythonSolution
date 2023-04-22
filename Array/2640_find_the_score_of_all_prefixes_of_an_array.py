from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = list()
        pre_mx = mx = pre_sum = 0
        for x in nums:
            mx = max(pre_mx, x)
            res.append(pre_sum + x + mx)
            pre_sum += x + mx
            pre_mx = mx
        return res


def test_find_prefix_score():
    solution = Solution()
    assert solution.findPrefixScore([2, 3, 7, 5, 10]) == [4, 10, 24, 36, 56], 'wrong result'
    assert solution.findPrefixScore([1, 1, 2, 4, 8, 16]) == [2, 4, 8, 16, 32, 64], 'wrong result'


if __name__ == '__main__':
    test_find_prefix_score()
