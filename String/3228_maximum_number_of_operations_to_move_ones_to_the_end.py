class Solution:
    def maxOperations(self, s: str) -> int:
        res, ones = 0, 0
        pre = ''
        for c in s:
            if c == '1':
                if pre == '0':
                    res += ones
                ones += 1
                pre = '1'
            else:
                pre = '0'
        return res + (ones if pre == '0' else 0)


def test_max_operations():
    solution = Solution()
    assert solution.maxOperations("110") == 2, 'wrong result'
    assert solution.maxOperations("1001101") == 4, 'wrong result'
    assert solution.maxOperations("00111") == 0, 'wrong result'


if __name__ == '__main__':
    test_max_operations()
