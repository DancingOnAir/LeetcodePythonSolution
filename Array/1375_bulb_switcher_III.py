from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
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
