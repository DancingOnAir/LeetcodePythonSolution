from typing import List


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        new_parent = parent[:]
        cnt = [1] * n

        for i in range(1, n):
            p = parent[i]
            while p != -1:
                if s[p] != s[i]:
                    p = parent[p]
                else:
                    new_parent[i] = p
                    break

        for i in range(1, n):
            p = new_parent[i]
            while p != -1:
                cnt[p] += 1
                p = new_parent[p]
        return cnt


def test_find_subtree_sizes():
    solution = Solution()
    assert solution.findSubtreeSizes([-1, 0, 0, 1, 1, 1], "abaabc") == [6, 3, 1, 1, 1, 1], 'wrong result'
    assert solution.findSubtreeSizes([-1, 0, 4, 0, 1], "abbba") == [5, 2, 1, 1, 1], 'wrong result'


if __name__ == '__main__':
    test_find_subtree_sizes()
