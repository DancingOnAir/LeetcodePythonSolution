from typing import List


class Solution:
    # https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/solutions/5904140/java-c-python-low-bit-o-n/
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if x & 1:
                res.append(x - ((x + 1) & (-x - 1)) // 2)
            else:
                res.append(-1)
        return res

    def minBitwiseArray1(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if x & 1:
                i = 1
                while (x >> i) & 1:
                    i += 1
                res.append(x ^ (1 << (i - 1)))
            else:
                res.append(-1)
        return res


def test_min_bitwise_array():
    solution = Solution()
    assert solution.minBitwiseArray([2, 3, 5, 7]) == [-1, 1, 4, 3], 'wrong result'
    assert solution.minBitwiseArray([11, 13, 31]) == [9, 12, 15], 'wrong result'


if __name__ == '__main__':
    test_min_bitwise_array()
