class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if str(i) * 3 in num:
                return str(i) * 3
        return ""

    def largestGoodInteger1(self, num: str) -> str:
        res = ''
        left = 0
        for right in range(1, len(num)):
            if num[left] != num[right]:
                left = right
            if right - left == 2:
                res = max(res, num[left: right + 1])
        return res


def test_largest_good_integer():
    solution = Solution()
    assert solution.largestGoodInteger("6777133339") == '777', 'wrong result'
    assert solution.largestGoodInteger("2300019") == '000', 'wrong result'
    assert solution.largestGoodInteger("42352338") == '', 'wrong result'


if __name__ == '__main__':
    test_largest_good_integer()
