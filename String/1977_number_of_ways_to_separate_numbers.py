class Solution:
    def numberOfCombinations(self, num: str) -> int:
        pass


def test_number_of_combinations():
    solution = Solution()
    assert solution.numberOfCombinations("327") == 2, 'wrong result'
    assert solution.numberOfCombinations("094") == 0, 'wrong result'
    assert solution.numberOfCombinations("0") == 0, 'wrong result'
    assert solution.numberOfCombinations("9999999999999") == 101, 'wrong result'


if __name__ == '__main__':
    test_number_of_combinations()
