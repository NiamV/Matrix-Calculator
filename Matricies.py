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
        k = 0
        for i in self.entries:
            if k == 0:
                row = "/   "
            elif k == len(self.entries) - 1:
                row = "\   " 
            else:
                row = "|   "

            for j in i:
                noSpaces = 6 - len(str(j))
                space = "  "
                for i in range(0,noSpaces):
                    space += " "
                row = row + str(j) + space
            
            if k == 0:
                row = row + "\ "
            elif k == len(self.entries) - 1:
                row = row + "/ "
            else:
                row = row + "| " 
            
            print(row)
            k += 1

    #Finds the determinant of the matrix - works for any size of square matrix
    def determinant(self):
        if len(self.entries) != len(self.entries):    #Check to see if the matrix is square
            print("No determinant exists as the matrix is not square")
        else:
            if len(self.entries) == 1:
                det = self.entries[0][0]
                return det
            
            elif len(self.entries) == 2:    #Determinant of a 2 by 2 matrix formula
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

def Transpose(Matrix1):
    transposeMatrixEntries = []
    for i in range(0,Matrix1.Columns()):
        newRow = []
        for j in range(0,Matrix1.Rows()):
            newRow.append(Matrix1.entries[j][i])
        transposeMatrixEntries.append(newRow)
    transposeMatrix = Matrix(transposeMatrixEntries)
    return transposeMatrix

def inverseMatrix(Matrix1):
    #Check to see if the matrix is square
    if Matrix1.Rows() != Matrix1.Columns():    
        return "No inverse exists as the matrix is not square"
    else:
        det = Matrix1.determinant()
        size = Matrix1.Rows()
        
        #Check to see if the determinant of the matrix is 0
        if det == 0:
            return "No inverse exists as the matrix is singular"
        else:
            #Create matrix of cofactors
            cofactorMatrixEntries = []
            for i in range(0,size):         #Rows
                nextRow = []
                for j in range(0,size):     #Columns
                    
                    #Creates the minor
                    newEntries = []
                    for p in Matrix1.entries:
                        row = []
                        for q in p:
                            row.append(q)
                        newEntries.append(row)
                    
                    #Removes the jth entry in each row
                    for row in newEntries:
                        del row[j]

                    #Removes the ith row
                    del newEntries[i]

                    Minor = Matrix(newEntries)
                    #Divide the minors by the determinant of the original matrix
                    cell = round(float(Minor.determinant())/float(det),3)

                    #Multiplies minor by -1 if necessary to get cofactor
                    if (i + j) % 2 == 1:
                        cell *= -1

                    nextRow.append(cell)
                cofactorMatrixEntries.append(nextRow)
            cofactorMatrix = Matrix(cofactorMatrixEntries)

            #Transpose the cofactor matrix
            inverse = Transpose(cofactorMatrix)
            return inverse    
                      
M1 = Matrix([[1,2,4,-2],[-2,3,5,2],[2,-2,1,-1],[-2,-4,3,1]])

print(inverseMatrix(M1).printMatrix())







