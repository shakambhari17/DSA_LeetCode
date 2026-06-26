class Solution:
    def findContentChildren(self, g, s):

        # Sort greed factors and cookies
        g.sort()
        s.sort()

        i = 0   # child pointer
        j = 0   # cookie pointer

        while i < len(g) and j < len(s):

            # Cookie can satisfy the child
            if s[j] >= g[i]:
                i += 1

            # Move to next cookie
            j += 1

        return i