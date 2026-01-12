from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = list()
        three = 3
        five = 5
        for i in range(1, n + 1):
            if i == three == five:
                res.append('FizzBuzz')
                three += 3
                five += 5
            elif i == three:
                res.append('Fizz')
                three += 3
            elif i == five:
                res.append('Buzz')
                five += 5
            else:
                res.append(str(i))
        return res

    # straight forward
    def fizzBuzz1(self, n: int) -> List[str]:
        res = list()
        for i in range(1, n + 1):
            if i % 15 == 0:
                res.append("FizzBuzz")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res


def test_fizz_buzz():
    solution = Solution()
    assert solution.fizzBuzz(3) == ["1", "2", "Fizz"], 'wrong result'
    assert solution.fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"], 'wrong result'
    assert solution.fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz",
                                     "13", "14", "FizzBuzz"], 'wrong result'


if __name__ == '__main__':
    test_fizz_buzz()
