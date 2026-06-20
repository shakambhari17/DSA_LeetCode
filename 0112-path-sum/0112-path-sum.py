class Solution:
    def hasPathSum(self, root, targetSum):

        # Base case
        if root is None:
            return False

        # Check if it is a leaf node
        if root.left is None and root.right is None:
            return targetSum == root.val

        # Search in left or right subtree
        return (
            self.hasPathSum(root.left, targetSum - root.val)
            or
            self.hasPathSum(root.right, targetSum - root.val)
        )
