from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        for i, v in enumerate(nums):
            nums[i] = (i, v)
        nums.sort(key=lambda x: x[1], reverse=True)

        for i, num in enumerate(nums):
            if i == 0:
                root = TreeNode(num[1])
            else:
                node = root


        pass


def test_construct_maximum_binary_tree():
    solution = Solution()
    assert solution.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]).val == 6, 'wrong result'
    assert solution.constructMaximumBinaryTree([3, 2, 1]).val == 3, 'wrong result'


if __name__ == '__main__':
    test_construct_maximum_binary_tree()
