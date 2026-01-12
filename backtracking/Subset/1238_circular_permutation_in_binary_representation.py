from typing import List


class Solution:
    # gray code
    # https://leetcode.com/problems/circular-permutation-in-binary-representation/solutions/414203/java-c-python-4-line-gray-code/
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return list(map(lambda x: start ^ x ^ (x >> 1), range(2 ** n)))

    # backtracking
    # TLE
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = [start]

        def valid(a, b):
            return bin(a ^ b)[2:].count('1') == 1

        def dfs(i, s):
            if len(res) == 2 ** n:
                if valid(res[0], res[-1]):
                    return True

            for j in s:
                if valid(res[-1], j):
                    res.append(j)
                    if dfs(i + 1, s - {j}):
                        return True
                    res.pop()
            return False

        dfs(1, set(range(2 ** n)) - {start})
        return res


def test_circular_permutation():
    solution = Solution()
    assert solution.circularPermutation(2, 3) == [3, 2, 0, 1], 'wrong result'
    assert solution.circularPermutation(3, 2) == [2, 6, 7, 5, 4, 0, 1, 3], 'wrong result'


if __name__ == '__main__':
    test_circular_permutation()
