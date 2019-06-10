class Matrix(object):
    #Entries need to be inputted as a list of lists of entries in a row
    def __init__(self,entries):
        self.entries = entries

    #Returns the number of rows in the matrix
    def Rows(self):
        return len(self.entries)

    #Returns the number of columns in the matrix
    def Columns(self):
        return len(self.entries[0])
    
    #Prints out the matrix
    def printMatrix(self):
        for i in self.entries:
            row = "|    "
            for j in i:
                noSpaces = 6 - len(str(j))
                space = ""
                for i in range(0,noSpaces):
                    space += " "
                row = row + str(j) + space
            row = row + "|"
            print(row)

    #Finds the determinant of the matrix - works for any size of square matrix
    def determinant(self):
        if len(self.entries) != len(self.entries[1]):    #Check to see if the matrix is square
            print("No determinant exists as the matrix is not square")
        else:
            if len(self.entries) == 2:    #Determinant of a 2 by 2 matrix formula
                det = self.entries[0][0]*self.entries[1][1] - self.entries[1][0]*self.entries[0][1]
                return det
            
            else:
                currentDet = 0
                for i in range(0,len(self.entries)):    #Recusive formula for the determinant, going along the top row
                    newMatrixEntries = []
                    
                    #Iterates over every row apart from the top row
                    for j in range(1,len(self.entries)):
                        nextRow = []
                        
                        #Iterates over every column and adds the value into the nextRow list
                        for k in range(0,len(self.entries)):
                            if k != i:
                                nextRow.append(self.entries[j][k])
                        newMatrixEntries.append(nextRow)
                    
                    #Defines a new matrix without the top row and column containing the ith value
                    newMatrix = Matrix(newMatrixEntries)
                    
                    #Creates a multiplier for whether you add or subtract the smaller determinant
                    if i % 2 == 0:
                        multiplier = 1
                    else:
                        multiplier = -1
                    
                    #Applies the recursive forumla
                    currentDet += int(newMatrix.determinant()) * self.entries[0][i] * multiplier
                return currentDet

def multiplyMatricies(Matrix1, Matrix2):
    #Check to see if the matricies can be multiplied
    if Matrix1.Columns() != Matrix2.Rows():
        return "The matrixies are not multiplicatively conformable"
    else:
        productMatrixEntries = []
        
        #Finds the entries for each cell of the product matrix and forms a list
        for i in range (0,Matrix1.Rows()):
            productMatrixRow = []
            for j in range(0,Matrix2.Columns()):
                entry = 0
                for k in range(0,Matrix1.Columns()):
                    entry += Matrix1.entries[i][k] * Matrix2.entries[k][j]
                productMatrixRow.append(entry)
            productMatrixEntries.append(productMatrixRow)

        return Matrix(productMatrixEntries)

M1 = Matrix([[1,2],[2,1],[-1,3]])
M2 = Matrix([[3,2,5],[-2,1,-2]])

print(multiplyMatricies(M1,M2).printMatrix())




