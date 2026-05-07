class Solution:
    def countCommas(self, n: int) -> int:
        res = 0
        low = 1000
        while low <= n:
            res += n - low + 1
            low *= 1000
        return res


def test_count_commas():
    solution = Solution()
    assert solution.countCommas(100000) == 99001, 'wrong result'
    assert solution.countCommas(1002) == 3, 'wrong result'
    assert solution.countCommas(998) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_commas()
