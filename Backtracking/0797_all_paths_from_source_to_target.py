from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        path = [0]

        def dfs(i):
            if i == n - 1:
                res.append(path.copy())
                return

            for j in graph[i]:
                path.append(j)
                dfs(j)
                path.pop()

        dfs(0)
        return res


def test_all_path_source_target():
    solution = Solution()
    assert solution.allPathsSourceTarget([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]], 'wrong result'
    assert solution.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]) == [[0, 4], [0, 3, 4], [0, 1, 3, 4],
                                                                                   [0, 1, 2, 3, 4],
                                                                                   [0, 1, 4]], 'wrong result'


if __name__ == '__main__':
    test_all_path_source_target()
