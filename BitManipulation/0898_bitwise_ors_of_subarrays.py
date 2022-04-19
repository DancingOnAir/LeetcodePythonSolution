from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        s, res = set(), set()
        for a in arr:
            s = {a | b for b in s} | {a}
            res |= s
        return len(res)


def test_subarray_bitwise_ors():
    solution = Solution()
    assert solution.subarrayBitwiseORs([0]) == 1, 'wrong result'
    assert solution.subarrayBitwiseORs([1, 1, 2]) == 3, 'wrong result'
    assert solution.subarrayBitwiseORs([1, 2, 4]) == 6, 'wrong result'


if __name__ == '__main__':
    test_subarray_bitwise_ors()
