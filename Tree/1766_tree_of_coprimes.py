from typing import List


class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def gcd(a, b):
            if a < b:
                a, b = b, a
            if a % b == 0:
                return b
            return gcd(b, a % b)

        def inorder(node, parent, path):
            if parent != -1:
                for p in path[::-1]:
                    if gcd(nums[node], nums[p]) == 1:
                        res[node] = p
                        break
                else:
                    res[node] = -1

            path.append(node)
            for child in graph[node]:
                if child != parent:
                    inorder(child, node, path)
                    path.pop()

        res = [-1] * n
        inorder(0, -1, [])
        return res


def test_get_coprimes():
    solution = Solution()
    assert solution.getCoprimes([2, 3, 3, 2], [[0, 1], [1, 2], [1, 3]]) == [-1, 0, 0, 1], 'wrong result'
    assert solution.getCoprimes([5, 6, 10, 2, 3, 6, 15], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]) == [-1, 0, -1, 0, 0, 0, -1], 'wrong result'


if __name__ == '__main__':
    test_get_coprimes()

