from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        return [num//3 - 1, num//3, num//3 + 1]


def test_sum_of_three():
    solution = Solution()
    assert solution.sumOfThree(33) == [10, 11, 12], 'wrong result'
    assert solution.sumOfThree(4) == [], 'wrong result'


if __name__ == '__main__':
    test_sum_of_three()
