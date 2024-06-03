from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        m = set()
        res = 0
        for x in nums:
            if x in m:
                res ^= x
            m.add(x)
        return res

    def duplicateNumbersXOR1(self, nums: List[int]) -> int:
        m = set()
        res = 0
        for x in nums:
            if x not in m:
                res ^= x
                m.add(x)
            res ^= x
        return res


def test_duplicate_numbers_xor():
    solution = Solution()
    assert solution.duplicateNumbersXOR([1, 2, 1, 3]) == 1, 'wrong result'
    assert solution.duplicateNumbersXOR([1, 2, 3]) == 0, 'wrong result'
    assert solution.duplicateNumbersXOR([1, 2, 2, 1]) == 3, 'wrong result'


if __name__ == '__main__':
    test_duplicate_numbers_xor()
