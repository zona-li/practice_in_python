from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        paths = {}

        def storePath(node: TreeNode, path: str):
            if node:
                paths[node.val] = path
                storePath(node.left, path + 'l')
                storePath(node.right, path + 'r')

        storePath(root, '')
        targetPath = paths[target.val]
        res = []
        for value, path in paths.items():
            i = 0
            while i < len(path) and i < len(targetPath) and path[i] == targetPath[i]:
                i += 1
            if len(targetPath[i:]) + len(path[i:]) == k:
                res.append(value)
        return res
