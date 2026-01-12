from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []

        res = []
        path = []

        def dfs(i, tot):
            if tot == 0:
                nonlocal res
                res = path.copy()
                return True

            for j in range(i, tot + 1, 2):
                if j <= tot:
                    path.append(j)
                    if dfs(j + 2, tot - j):
                        return True
                    path.pop()

            return False

        if dfs(2, finalSum):
            return res
        return res


def test_maximum_even_split():
    solution = Solution()
    assert solution.maximumEvenSplit(12) == [2, 4, 6], 'wrong result'
    assert solution.maximumEvenSplit(7) == [], 'wrong result'
    assert solution.maximumEvenSplit(28) == [2, 4, 6, 16], 'wrong result'


if __name__ == '__main__':
    test_maximum_even_split()
