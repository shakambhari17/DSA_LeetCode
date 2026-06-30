class Solution:
    def combinationSum(self, candidates, target):

        result = []

        def backtrack(start, path, total):

            # Found the target
            if total == target:
                result.append(path[:])
                return

            # Sum exceeded target
            if total > target:
                return

            # Try every candidate
            for i in range(start, len(candidates)):

                # Choose
                path.append(candidates[i])

                # Explore
                backtrack(i, path, total + candidates[i])

                # Undo (Backtrack)
                path.pop()

        backtrack(0, [], 0)

        return result