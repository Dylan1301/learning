class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefixMatrix()
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 or col1 == 0:
            upperleft = 0
        else:
            upperleft = self.matrix[row1-1][col1-1]
        if col1 == 0:
            lowerleft = 0
        else:
            lowerleft = self.matrix[row2][col1-1]
        
        if row1 == 0:
            upperright = 0
        else:
            upperright = self.matrix[row1-1][col2]
        
        return self.matrix[row2][col2] + upperleft - lowerleft  - upperright


    
    def prefixMatrix(self):
        rows, cols = len(self.matrix), len(self.matrix[0])

        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    prefixcol = 0
                else:
                    prefixcol =  self.matrix[i-1][j]
                if j == 0:
                    prefixrow = 0
                else:
                    prefixrow = self.matrix[i][j-1]
                if i != 0  and j!=0:
                    prefixdiag = self.matrix[i-1][j-1]
                else:
                    prefixdiag = 0
                
                self.matrix[i][j] = self.matrix[i][j] + prefixcol + prefixrow - prefixdiag
            

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)