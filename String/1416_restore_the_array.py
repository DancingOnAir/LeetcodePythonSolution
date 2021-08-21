class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        pass


def test_number_of_arrays():
    solution = Solution()

    assert solution.numberOfArrays("1000", 1000) == 1, 'wrong result'
    assert solution.numberOfArrays("1000", 10) == 0, 'wrong result'
    assert solution.numberOfArrays("1317", 2000) == 8, 'wrong result'
    assert solution.numberOfArrays("2020", 30) == 1, 'wrong result'
    assert solution.numberOfArrays("1234567890", 90) == 34, 'wrong result'


if __name__ == '__main__':
    test_number_of_arrays()
