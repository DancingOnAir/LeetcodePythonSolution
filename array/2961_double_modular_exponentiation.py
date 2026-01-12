from typing import List


class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        return [i for i, (a, b, c, m) in enumerate(variables) if pow(pow(a, b, 10), c, m) == target]

    def getGoodIndices1(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, (a, b, c, m) in enumerate(variables):
            if ((a ** b % 10) ** c) % m == target:
                res.append(i)
        return res


def test_get_good_indices():
    solution = Solution()
    assert solution.getGoodIndices([[2, 3, 3, 10], [3, 3, 3, 1], [6, 1, 1, 4]], 2) == [0, 2], 'wrong result'
    assert solution.getGoodIndices([[39, 3, 1000, 1000]], 17) == [], 'wrong result'


if __name__ == '__main__':
    test_get_good_indices()
