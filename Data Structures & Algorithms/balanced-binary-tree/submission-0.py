class Solution:

    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(node: TreeNode | None) -> tuple[bool, int]:
            if not node:
                return True, 0

            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )
            height = 1 + max(left_height, right_height)

            return balanced, height

        return dfs(root)[0]