from typing import List


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u,  v in edges:
            g[u].append(v)
            g[v].append(u)

        res = 0
        seen = set()
        for i in range(n):
            if i not in seen:
                seen.add(i)
                cnt = 1
                q = [i]
                while q:
                    u = q.pop()
                    for v in g[u]:
                        if v not in seen:
                            seen.add(v)
                            q.append(v)
                            cnt += 1
                n -= cnt
                res += n * cnt

        return res


def test_count_pairs():
    solution = Solution()
    assert solution.countPairs(12, []) == 66, 'wrong result'
    assert solution.countPairs(3, [[0, 1], [0, 2], [1, 2]]) == 0, 'wrong result'
    assert solution.countPairs(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]) == 14, 'wrong result'


if __name__ == '__main__':
    test_count_pairs()
