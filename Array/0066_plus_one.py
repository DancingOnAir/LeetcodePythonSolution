from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i, val in enumerate(digits):
            num += val * pow(10, len(digits) - i - 1)
        return [int(i) for i in str(num + 1)]

    def plusOne2(self, digits: List[int]) -> List[int]:
        n = len(digits)
        extra = 0
        for i, val in enumerate(digits[::-1]):
            num = val + extra
            if not i:
                num += 1
            if num > 9:
                digits[n - i - 1] = num % 10
                extra = 1
            else:
                digits[n - i - 1] = num
                extra = 0
                break
        return digits if not extra else [1] + digits

    def plusOne1(self, digits: List[int]) -> List[int]:
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

    digits2 = [4, 3, 2, 1]
    print(solution.plusOne(digits2))

    digits3 = [0]
    print(solution.plusOne(digits3))

    digits4 = [9, 9]
    print(solution.plusOne(digits4))


if __name__ == '__main__':
    test_plus_one()
