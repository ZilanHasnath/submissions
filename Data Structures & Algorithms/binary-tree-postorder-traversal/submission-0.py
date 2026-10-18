class Solution:

    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return result[::-1]