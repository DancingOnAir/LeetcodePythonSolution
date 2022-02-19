class Solution:
    def minimumTime(self, s: str) -> int:
        pass


def test_minimum_time():
    solution = Solution()
    assert solution.minimumTime('1100101') == 5, 'wrong result'
    assert solution.minimumTime('0010') == 2, 'wrong result'


if __name__ == '__main__':
    test_minimum_time()
