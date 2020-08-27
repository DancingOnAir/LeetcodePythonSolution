from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i, val in enumerate(digits):
            num = num * 10 + val
        num += 1

        res = []
        while num:
            res = [num % 10] + res
            num //= 10
        return res


def test_plus_one():
    solution = Solution()

    digits1 = [1, 2, 3]
    print(solution.plusOne(digits1))

    digits2 = [4,3,2,1]
    print(solution.plusOne(digits2))

    digits3 = [0]
    print(solution.plusOne(digits3))
    pass


if __name__ == '__main__':
    test_plus_one()
