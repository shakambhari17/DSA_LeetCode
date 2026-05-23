class Solution(object):
    def diagonalSum(self, mat):

        left_sum=0
        right_sum=0

        n=len(mat)

        for i in range(n):
            left_sum=left_sum + mat[i][i]
            right_sum=right_sum + mat[i][n-1-i]
        result = abs(left_sum + right_sum)
        if n%2==1:
            result -= mat[n//2][n//2]
        return result
        
    

       
        