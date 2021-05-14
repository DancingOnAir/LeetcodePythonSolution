class Solution:
    def maxDiff(self, num: int) -> int:
        max_num_digit = min_num_digit = ''
        min_digit = 1
        res = 0
        for i, c in enumerate(str(num)):
            if not max_num_digit:
                if c != '9':
                    max_num_digit = c
            if not min_num_digit:
                if i == 0 and c > '1':
                    min_num_digit = c
                elif i > 0 and c > '1':
                    min_num_digit = c
                    min_digit = 0

            cur = 0
            if c == max_num_digit:
                cur += int('9') - int(c)
            if c == min_num_digit:
                cur += int(c) - int(min_digit)
            res = res * 10 + cur
        return res


def test_max_diff():
    solution = Solution()
    assert solution.maxDiff(555) == 888, 'wrong result'
    assert solution.maxDiff(9) == 8, 'wrong result'
    assert solution.maxDiff(123456) == 820000, 'wrong result'
    assert solution.maxDiff(10000) == 80000, 'wrong result'
    assert solution.maxDiff(9288) == 8700, 'wrong result'
    assert solution.maxDiff(111) == 888, 'wrong result'


if __name__ == '__main__':
    test_max_diff()
