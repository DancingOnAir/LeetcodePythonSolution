class Solution:
    def countValidPrefixes(self, s: str) -> int:
        res = zeros = ones = 0
        for c in s:
            if c == '0':
                zeros += 1
            else:
                ones += 1
            if abs(zeros - ones) < 2:
                res += 1
        return res


def test_count_valid_prefixes():
    solution = Solution()
    assert solution.countValidPrefixes("00101") == 3, 'wrong result'
    assert solution.countValidPrefixes("101") == 3, 'wrong result'


if __name__ == '__main__':
    test_count_valid_prefixes()
