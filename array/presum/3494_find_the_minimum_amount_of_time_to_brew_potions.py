from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        last_finish = [0] * n
        for m in mana:
            sum_t = 0
            for x, last in zip(skill, last_finish):
                if last > sum_t:
                    sum_t = last
                sum_t += x * m
            last_finish[-1] = sum_t
            for i in range(n - 2, -1, -1):
                last_finish[i] = last_finish[i + 1] - skill[i + 1] * m
        return last_finish[-1]


def test_min_time():
    solution = Solution()
    assert solution.minTime([1, 5, 2, 4], mana=[5, 1, 4, 2]) == 110, 'wrong result'
    assert solution.minTime([1, 1, 1], mana=[1, 1, 1]) == 5, 'wrong result'
    assert solution.minTime([1, 2, 3, 4], mana=[1, 2]) == 21, 'wrong result'


if __name__ == '__main__':
    test_min_time()
