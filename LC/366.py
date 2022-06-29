class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result_map = collections.defaultdict(list)
        
        def dfs(node, level):
            if not node:
                return level
            currLevel = max(dfs(node.left, level), dfs(node.right, level))
            result_map[currLevel].append(node.val)
            return currLevel + 1
        
        dfs(root, 0)
        print(result_map)
        return result_map.values()