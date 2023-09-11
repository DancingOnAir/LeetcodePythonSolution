from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        path = [0]

        def valid(a, b):
            return bin(a ^ b)[2:].count('1') == 1

        def dfs(i, s):
            if i == 2 ** n - 1:
                if valid(path[0], path[-1]):
                    nonlocal res
                    res = path[:]
                return

            for c in s:
                if valid(path[-1], c):
                    path.append(c)
                    dfs(i + 1, s - {c})
                    path.pop()
        dfs(0, set(range(1, 2 ** n)))
        return res


def test_gray_code():
    solution = Solution()
    assert solution.grayCode(2) == [0, 1, 3, 2], 'wrong result'
    assert solution.grayCode(1) == [0, 1], 'wrong result'


if __name__ == '__main__':
    test_gray_code()
