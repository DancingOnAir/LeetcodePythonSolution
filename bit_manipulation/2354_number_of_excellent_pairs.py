import tkinter
from typing import List
from collections import Counter


class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        c = list()
        for x in set(nums):
            c.append(bin(x).count('1'))

        c = Counter(c)
        return sum(c[k1] * c[k2] for k1 in c for k2 in c if k1 + k2 >= k)

    # TLE
    def countExcellentPairs1(self, nums: List[int], k: int) -> int:
        bits = [bin(x).count('1') for x in nums]
        res = 0
        seen = set()
        for i in range(len(bits)):
            for j in range(len(bits)):
                if (nums[i], nums[j]) not in seen:
                    seen.add((nums[i], nums[j]))
                    if bits[i] + bits[j] >= k:
                        res += 1
        return res


def test_count_excellent_pairs():
    solution = Solution()
    assert solution.countExcellentPairs([1, 2, 3, 1], 3) == 5, 'wrong result'
    assert solution.countExcellentPairs([5, 1, 1], 10) == 0, 'wrong result'


if __name__ == '__main__':
    test_count_excellent_pairs()
