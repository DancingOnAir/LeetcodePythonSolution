class Solution:
    def regionsBySlashes(self, grid: list[str]) -> int:
        n = len(grid)
        parents = [i for i in range(4 * n * n)]

        def find(p):
            while parents[p] != p:
                parents[p] = parents[parents[p]]
                p = parents[p]
            return p

        def unite(p, q):
            parents[find(p)] = parents[find(q)]

        res = 0
        for i in range(n):
            for j in range(n):
                x0, x1, x2, x3 = (i * n + j) * 4, (i * n + j) * 4 + 1, (i * n + j) * 4 + 2, (i * n + j) * 4 + 3
                if i > 0:
                    ux2 = ((i - 1) * n + j) * 4 + 2
                    unite(ux2, x0)
                if j > 0:
                    ux1 = (i * n + j - 1) * 4 + 1
                    unite(ux1, x3)
                if grid[i][j] == ' ':
                    unite(x0, x1)
                    unite(x0, x2)
                    unite(x0, x3)
                elif grid[i][j] == '/':
                    unite(x0, x3)
                    unite(x1, x2)
                else:
                    unite(x0, x1)
                    unite(x2, x3)
        return sum(find(i) == i for i in range(len(parents)))


def test_regions_by_slashes():
    solution = Solution()
    assert solution.regionsBySlashes([" /", "/ "]) == 2, 'wrong result'
    assert solution.regionsBySlashes([" /", "  "]) == 1, 'wrong result'
    assert solution.regionsBySlashes(["/\\", "\\/"]) == 5, 'wrong result'


if __name__ == '__main__':
    test_regions_by_slashes()
