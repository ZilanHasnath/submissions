class Solution:

    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result