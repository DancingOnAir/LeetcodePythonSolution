from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 下面贪婪后续遍历解法的优化
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def postorder(root: Optional[TreeNode]):
            if not root:
                return 2

            left, right = postorder(root.left), postorder(root.right)
            if left == 3 or right == 3:
                self.res += 1
                return 1
            return 2 if left == 1 or right == 1 else 3

        self.res = 0
        return (postorder(root) == 3) + self.res

    # 贪婪，叶子节点不放监控是最优解法，从叶子节点往上处理，那么选择后序遍历
    # 每个节点的3种状态：1.有摄像头，2.无摄像头，但是已被摄像头覆盖，3.无摄像头，也没被摄像头覆盖
    # 初始状态，None，因为需要叶子节点的父节点有摄像头，那么叶子节点是状态3，所以None节点不能有摄像头，也不能无摄像头五覆盖，只能状态2
    def minCameraCover2(self, root: Optional[TreeNode]) -> int:
        def postorder(root):
            if not root:
                return 2

            left = postorder(root.left)
            right = postorder(root.right)

            if left == 2 and right == 2:
                return 3
            elif left == 3 or right == 3:
                self.res += 1
                return 1
            elif left == 1 or right == 1:
                return 2
            return -1

        self.res = 0
        # 最后根节点无覆盖需要多放1个摄像头
        if postorder(root) == 3:
            self.res += 1

        return self.res

    # a: root必须放置1个摄像头的情况下，覆盖以root为根节点的整棵树需要的摄像头数目
    # b: 无论root是否安放摄像头，覆盖以root为根节点的整棵树需要的摄像头数目
    # c: 无论root本身是否被监控，覆盖root的两颗子树需要的摄像头数目
    # a >= b >= c
    def minCameraCover1(self, root: Optional[TreeNode]) -> int:
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
