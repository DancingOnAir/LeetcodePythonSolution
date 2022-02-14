class Solution:
    def numberOfWays(self, corridor: str) -> int:
        pass


def test_number_of_ways():
    solution = Solution()
    assert solution.numberOfWays('SSPPSPS') == 3, 'wrong reuslt'
    assert solution.numberOfWays('PPSPSP') == 1, 'wrong reuslt'
    assert solution.numberOfWays('S') == 0, 'wrong reuslt'


if __name__ == '__main__':
    test_number_of_ways()
