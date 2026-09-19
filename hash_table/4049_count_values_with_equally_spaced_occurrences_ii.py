from collections import defaultdict
from itertools import pairwise


class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        cnt = defaultdict(list)
        for i, x in enumerate(nums):
            cnt[x].append(i)

        res = 0
        for k, v in cnt.items():
            if len(v) < 3:
                continue
            d = v[1] - v[0]
            if all(b - a == d for a, b in pairwise(v)):
                res += 1

        return res


def test_count_special_integers():
    solution = Solution()
    assert solution.countSpecialIntegers([1,8,1,5,1,5,8,5]) == 2, 'wrong result'
    assert solution.countSpecialIntegers([8,8,8,8]) == 1, 'wrong result'
    assert solution.countSpecialIntegers([8,6,6,8,8]) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_special_integers()
