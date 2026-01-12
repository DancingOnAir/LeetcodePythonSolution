from typing import List
from collections import Counter


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        return sum(((v + k) // (k + 1) * (k + 1)) for k, v in cnt.items())

    def numRabbits1(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        res = 0
        for k, v in cnt.items():
            q, r = divmod(v, k + 1)
            res += q * (k + 1)
            if r > 0:
                res += k + 1
        return res


def test_num_rabbits():
    solution = Solution()
    # assert solution.numRabbits([1, 1, 2]) == 5, 'wrong result'
    assert solution.numRabbits([10, 10, 10]) == 11, 'wrong result'


if __name__ == '__main__':
    test_num_rabbits()
