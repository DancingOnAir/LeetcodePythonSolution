from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(idx):
            if idx != uf[idx]:
                idx = find(uf[idx])
            return idx

        uf = {i: i for i in range(len(isConnected))}
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    uf[find(i)] = find(j)
        return len([x for x in uf if uf[x] == x])

    def findCircleNum1(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        if 1 == n:
            return 1

        parents = list(range(200))

        def find(idx):
            while idx != parents[idx]:
                idx = parents[idx]
            return idx

        def union(idx1, idx2):
            p1 = find(idx1)
            p2 = find(idx2)
            if p1 == p2:
                return
            parents[p1] = p2

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        res = set()
        for i in range(n):
            if find(i) not in res:
                res.add(find(i))
        return len(res)


def test_find_circle_num():
    solution = Solution()

    assert solution.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]) == 1, 'wrong result'
    assert solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2, 'wrong result'
    assert solution.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3, 'wrong result'


if __name__ == '__main__':
    test_find_circle_num()
