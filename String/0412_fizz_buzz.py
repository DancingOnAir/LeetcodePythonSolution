from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        pass


def test_fizz_buzz():
    solution = Solution()
    assert solution.fizzBuzz(3) == ["1", "2", "Fizz"], 'wrong result'
    assert solution.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"], 'wrong result'
    assert solution.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz",
                                     "13", "14", "FizzBuzz"], 'wrong result'


if __name__ == '__main__':
    test_fizz_buzz()
