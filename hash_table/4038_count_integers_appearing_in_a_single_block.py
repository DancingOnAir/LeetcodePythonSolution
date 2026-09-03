from collections import Counter
from itertools import groupby


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        cnt = Counter(x for x, _ in groupby(nums))
        return sum(1 for x in cnt if cnt[x] == 1)


def test_count_speical_integers():
    solution = Solution()
    assert solution.countSpecialIntegers([1, 2, 2, 1]) == 1, 'wrong result'
    assert solution.countSpecialIntegers([3, 3, 1, 2, 2, 1]) == 2, 'wrong result'


if __name__ == '__main__':
    test_count_speical_integers()
