from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        leftNodes, rightNodes, children = [], [], []

        def leftBoundry(node: Optional[TreeNode]):
            if not node:
                return
            if not node.left and not node.right:
                return
            leftNodes.append(node.val)
            if node.left:
                leftBoundry(node.left)
            else:
                leftBoundry(node.right)

        def rightBoundry(node: Optional[TreeNode]):
            if not node:
                return
            if not node.left and not node.right:
                return
            rightNodes.append(node.val)
            if node.right:
                rightBoundry(node.right)
            else:
                rightBoundry(node.left)

        leftBoundry(root.left)
        rightBoundry(root.right)
        rightNodes.reverse()

        stack = [root.right, root.left]
        while stack:
            nextNode = stack.pop()
            if nextNode:
                if not nextNode.left and not nextNode.right:
                    children.append(nextNode.val)
                else:
                    stack.extend([nextNode.right, nextNode.left])

        print(leftNodes, rightNodes, children)
        return [root.val] + leftNodes + children + rightNodes


s = Solution()
print(s.boundaryOfBinaryTree())
