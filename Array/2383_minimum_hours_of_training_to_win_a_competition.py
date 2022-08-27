from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        max_energy = sum(energy)
        max_exp = pre_sum = 0
        for exp in experience:
            max_exp = max(max_exp, exp - pre_sum)
            pre_sum += exp

        res = 0
        if max_energy + 1 > initialEnergy:
            res += max_energy + 1 - initialEnergy
        if max_exp + 1 > initialExperience:
            res += max_exp + 1 - initialExperience
        return res


def test_min_number_of_hours():
    solution = Solution()
    assert solution.minNumberOfHours(1, 1, [1, 1, 1, 1], [1, 1, 1, 50]) == 51, 'wrong result'
    assert solution.minNumberOfHours(5, 3, [1, 4, 3, 2], [2, 6, 3, 1]) == 8, 'wrong result'
    assert solution.minNumberOfHours(2, 4, [1], [3]) == 0, 'wrong result'


if __name__ == '__main__':
    test_min_number_of_hours()
