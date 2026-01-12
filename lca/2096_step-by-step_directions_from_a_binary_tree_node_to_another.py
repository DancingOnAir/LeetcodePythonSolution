from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(r, val, path):
            if r.val == val:
                return True
            if r.left and dfs(r.left, val, path):
                path += 'L'
            elif r.right and dfs(r.right, val, path):
                path += 'R'
            return path

        start_path = list()
        dest_path = list()
        dfs(root, startValue, start_path)
        dfs(root, destValue, dest_path)

        while len(start_path) and len(dest_path) and start_path[-1] == dest_path[-1]:
            start_path.pop()
            dest_path.pop()
        return 'U' * len(start_path) + ''.join(reversed(dest_path))

    def getDirections1(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(c, r, depth, direct):
            if c is None:
                return

            parents[c] = r
            depths[c] = depth
            directions[c] = direct

            nonlocal start_node
            nonlocal dest_node
            if c.val == startValue:
                start_node = c
            elif c.val == destValue:
                dest_node = c

            dfs(c.left, c, depth+1, 'L')
            dfs(c.right, c, depth+1, 'R')

        def jump_parent(r, steps, path):
            while steps > 0:
                path.append(directions[r])
                r = parents[r]
                steps -= 1
            return r

        parents = dict()
        depths = dict()
        directions = dict()
        start_node = TreeNode()
        dest_node = TreeNode()

        dfs(root, None, 0, '')

        start_path = list()
        dest_path = list()
        if depths[start_node] < depths[dest_node]:
            dest_node = jump_parent(dest_node, depths[dest_node] - depths[start_node], dest_path)
        else:
            start_node = jump_parent(start_node, depths[start_node] - depths[dest_node], start_path)

        while start_node != dest_node:
            start_path.append('U')
            start_node = parents[start_node]

            dest_path.append(directions[dest_node])
            dest_node = parents[dest_node]

        dest_path.reverse()
        return 'U' * len(start_path) + ''.join(dest_path)


def test_get_directions():
    solution = Solution()

    node_list = [TreeNode(x) for x in range(7)]
    node_list[5].left = node_list[1]
    node_list[5].right = node_list[2]
    node_list[1].left = node_list[3]
    node_list[2].left = node_list[6]
    node_list[2].right = node_list[4]
    assert solution.getDirections(node_list[5], 3, 6) == "UURL", 'wrong result'

    node_list = [TreeNode(x) for x in range(3)]
    node_list[2].left = node_list[1]
    assert solution.getDirections(node_list[2], 2, 1) == "L", 'wrong result'


if __name__ == '__main__':
    test_get_directions()
