from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, idx=-1):
        self.val = val
        self.left = left
        self.right = right
        self.idx = idx


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            max_id, max_val = max(enumerate(nums), key=lambda x: x[1])
            return TreeNode(max_val, self.constructMaximumBinaryTree(nums[:max_id]), self.constructMaximumBinaryTree(nums[max_id+1:]))


def test_construct_maximum_binary_tree():
    solution = Solution()
    assert solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]).val == 6, 'wrong result'
    assert solution.constructMaximumBinaryTree([3, 2, 1]).val == 3, 'wrong result'


if __name__ == '__main__':
    test_construct_maximum_binary_tree()
