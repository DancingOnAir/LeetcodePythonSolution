from typing import List


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        i, j = len(arr1) - 1, len(arr2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            a = 0 if i < 0 else arr1[i]
            b = 0 if j < 0 else arr2[j]
            x = a + b + carry
            carry = 0
            if x >= 2:
                x -= 2
                carry -= 1
            elif x == -1:
                x = 1
                carry += 1
            res.append(x)
            i -= 1
            j -= 1
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]


def test_add_negabinary():
    solution = Solution()
    assert solution.addNegabinary([1], arr2=[1]) == [1, 1, 0], 'wrong result'
    assert solution.addNegabinary([1, 1, 1, 1, 1], arr2=[1, 0, 1]) == [1, 0, 0, 0, 0], 'wrong result'
    assert solution.addNegabinary([0], arr2=[0]) == [0], 'wrong result'
    assert solution.addNegabinary([0], arr2=[1]) == [1], 'wrong result'


if __name__ == '__main__':
    test_add_negabinary()
