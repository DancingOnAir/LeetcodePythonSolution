from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # recursive
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(pre, post):
            if not pre:
                return None
            root = TreeNode(pre[0])

            i = 1
            while i < len(pre):
                if len(set(pre[1: 1 + i]) - set(post[: i])) == 0:
                    break
                i += 1

            root.left = helper(pre[1: i+1], post[: i])
            root.right = helper(pre[i+1:], post[i: -1])
            return root

        return helper(preorder, postorder)


def test_construct_from_pre_post():
    solution = Solution()

    preorder = [1, 2, 4, 5, 3, 6, 7]
    postorder = [4, 5, 2, 6, 7, 3, 1]
    assert solution.constructFromPrePost(preorder, postorder).val == 1, 'wrong result'
    assert solution.constructFromPrePost(preorder, postorder).left.val == 2, 'wrong result'
    assert solution.constructFromPrePost(preorder, postorder).right.val == 3, 'wrong result'


if __name__ == '__main__':
    test_construct_from_pre_post()
