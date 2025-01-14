'''
time complexity: O(r+c)
r ,c - row and col of matrix
space complexity: O(1)
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #row
        m = len(matrix)
        n = len(matrix[0])
        
        i = 0
        j = n-1
        
        while(i<m and j>=0):
            if(matrix[i][j]==target): return True
            elif(matrix[i][j]<target): i+=1
            else: j-=1
        return False
                