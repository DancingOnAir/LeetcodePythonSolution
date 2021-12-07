from typing import List
from collections import Counter


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        freq = Counter(deliciousness)

        res = 0
        for x in freq:
            for k in range(22):
                if 2 ** k - x <= x:
                    if x == 2 ** (k - 1):
                        res += freq[x] * (freq[x] - 1) // 2
                    else:
                        res += freq[x] * freq[2 ** k - x]

        return res % (10 ** 9 + 7)


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs([1, 3, 5, 7, 9]) == 4, 'wrong result'
    assert solution.countPairs([1, 1, 1, 3, 3, 3, 7]) == 15, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()

