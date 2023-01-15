from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum(x & (1 << i) > 0 for x in candidates) for i in range(24))

    def largestCombination1(self, candidates: List[int]) -> int:
        res = 0
        for i in range(24):
            res = max(res, sum(1 for x in candidates if x & (1 << i)))
        return res


def test_largest_combination():
    solution = Solution()
    # 0001 0000, 0001 0001, 0100 0111, 0011 1110, 0000 0110, 0001 1000, 0000 1110
    assert solution.largestCombination([16, 17, 71, 62, 12, 24, 14]) == 4, 'wrong result'
    assert solution.largestCombination([8, 8]) == 2, 'wrong result'


if __name__ == '__main__':
    test_largest_combination()
