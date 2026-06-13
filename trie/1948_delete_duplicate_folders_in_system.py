from typing import List
from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.deleted = False


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        def add_path(path):
            t = root
            for s in path:
                if s not in t.children:
                    t.children[s] = Trie()
                t = t.children[s]

        def dfs1(node):
            s = "(" + "".join(c + dfs1(node.children[c]) for c in node.children) + ")"
            if s != "()":
                pattern[s].append(node)
            return s

        def dfs2(node, path):
            for c in node.children:
                if not node.children[c].deleted:
                    dfs2(node.children[c], path + [c])
            if path:
                res.append(path[:])

        root = Trie()
        pattern = defaultdict(list)
        res = []
        for path in sorted(paths):
            add_path(path)

        dfs1(root)
        for nodes in pattern.values():
            if len(nodes) > 1:
                for node in nodes:
                    node.deleted = True

        dfs2(root, [])
        return res


def test_delete_duplicate_folder():
    solution = Solution()
    assert solution.deleteDuplicateFolder(
        [["a"], ["c"], ["a", "b"], ["c", "b"], ["a", "b", "x"], ["a", "b", "x", "y"], ["w"], ["w", "y"]]) == [["c"],
                                                                                                              ["c",
                                                                                                               "b"],
                                                                                                              ["a"],
                                                                                                              ["a",
                                                                                                               "b"]], 'wrong result'
    assert solution.deleteDuplicateFolder([["a", "b"], ["c", "d"], ["c"], ["a"]]) == [["c"], ["c", "d"], ["a"],
                                                                                      ["a", "b"]], 'wrong result'


if __name__ == '__main__':
    test_delete_duplicate_folder()
