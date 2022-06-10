from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # a: root必须放置1个摄像头的情况下，覆盖整棵树需要的摄像头数目
    # b: 无论root是否安放摄像头，覆盖整棵树需要的摄像头数目
    # c: 无论root本身是否被监控，覆盖两颗子树需要的摄像头数目
    # a >= b >= c
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return float('inf'), 0, 0
            la, lb, lc = dfs(root.left)
            ra, rb, rc = dfs(root.right)

            a = 1 + lc + rc
            b = min(a, la + rb, lb + ra)
            c = min(a, lb + rb)
            return a, b, c

        a, b, c = dfs(root)
        return b


def test_min_camera_cover():
    solution = Solution()

    assert solution.minCameraCover(TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)))) == 1, 'wrong result'
    assert solution.minCameraCover(TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, None, TreeNode(0)))))) == 2, 'wrong result'


if __name__ == '__main__':
    test_min_camera_cover()
