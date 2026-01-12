from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        res, offset = 0, 0
        for x in sorted(happiness, reverse=True)[:k]:
            if x + offset <= 0:
                break

            res += x + offset
            offset -= 1
        return res


def test_maximum_happiness_sum():
    solution = Solution()
    assert solution.maximumHappinessSum([1, 2, 3], 2) == 4, 'wrong result'
    assert solution.maximumHappinessSum([1, 1, 1, 1], 2) == 1, 'wrong result'
    assert solution.maximumHappinessSum([2, 3, 4, 5], 1) == 5, 'wrong result'


if __name__ == '__main__':
    test_maximum_happiness_sum()
