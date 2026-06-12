
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return quadTree1.val and quadTree1 or quadTree2
        elif quadTree2.isLeaf:
            return quadTree2.val and quadTree2 or quadTree1
        else:
            top_left = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            top_right = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bottom_left = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bottom_right = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if top_left.isLeaf and top_right.isLeaf and bottom_left.isLeaf and bottom_right.isLeaf and top_left.val == top_right.val == bottom_left.val == bottom_right.val:
                return Node(top_left.val, True, None, None, None, None)
            return Node(0, False, top_left, top_right, bottom_left, bottom_right)


def test_intersect():
    solution = Solution()
    root1 = Node(0, True, None, None, None, None)
    root2 = Node(0, True, None, None, None, None)
    node = solution.intersect(root1, root2)
    assert node.isLeaf, 'wrong result'
    assert node.val == 0, 'wrong result'


if __name__ == '__main__':
    test_intersect()
