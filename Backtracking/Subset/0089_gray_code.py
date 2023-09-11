from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        path = [0]

        def valid(a, b):
            return bin(a ^ b)[2:].count('1') == 1

        def dfs(i, s):
            if len(path) == 2 ** n:
                if valid(path[0], path[-1]):
                    return True
                return False

            for c in s:
                if valid(path[-1], c):
                    path.append(c)
                    if dfs(i + 1, s - {c}):
                        return True
                    path.pop()
            return False

        dfs(0, set(range(1, 2 ** n)))
        return path


def test_gray_code():
    solution = Solution()
    assert solution.grayCode(2) == [0, 1, 3, 2], 'wrong result'
    assert solution.grayCode(1) == [0, 1], 'wrong result'


if __name__ == '__main__':
    test_gray_code()
