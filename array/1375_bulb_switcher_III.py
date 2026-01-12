from typing import List
from itertools import accumulate, count
from operator import eq


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        return sum(map(eq, accumulate(light, max), count(1)))

    def numTimesAllBlue3(self, light: List[int]) -> int:
        return sum(i == m for i, m in enumerate(accumulate(light, max), 1))

    def numTimesAllBlue2(self, light: List[int]) -> int:
        sum_i = sum_val = res = 0
        for i, val in enumerate(light, 1):
            sum_i += i
            sum_val += val
            res += sum_i == sum_val
        return res

    def numTimesAllBlue1(self, light: List[int]) -> int:
        right = res = 0
        for i, val in enumerate(light, 1):
            right = max(right, val)
            res += (right == i)
        return res


def test_num_times_all_blue():
    solution = Solution()

    light1 = [2, 1, 3, 5, 4]
    print(solution.numTimesAllBlue(light1))

    light2 = [3, 2, 4, 1, 5]
    print(solution.numTimesAllBlue(light2))

    light3 = [4, 1, 2, 3]
    print(solution.numTimesAllBlue(light3))

    light4 = [2, 1, 4, 3, 6, 5]
    print(solution.numTimesAllBlue(light4))

    light5 = [1, 2, 3, 4, 5, 6]
    print(solution.numTimesAllBlue(light5))


if __name__ == '__main__':
    test_num_times_all_blue()
