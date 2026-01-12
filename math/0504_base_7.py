class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return '0'
        sign = ""
        if num < 0:
            sign = "-"
        res = []
        num = abs(num)
        while num:
            num, q = divmod(num, 7)
            res.append(str(q))
        return sign + ''.join(res[::-1])


def test_convert_to_base_7():
    solution = Solution()
    assert solution.convertToBase7(100) == "202", 'wrong result'
    assert solution.convertToBase7(-7) == "-10", 'wrong result'


if __name__ == '__main__':
    test_convert_to_base_7()
