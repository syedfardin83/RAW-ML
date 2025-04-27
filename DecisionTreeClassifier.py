from random import randint


# We will write 2 functions:
# 1 -> The classifier which takes an m*n matrix train_set. 
#     m -> number of entries
#     n -> features
#     1 -> label(0 or 1)
    # and also takes a label matrix of order m*1 label_set
#     returns a decision tree which is a matrix
# 2 -> The result which takes in two matrix. A decision tree and a question matrix of order 1*(n) and returns a label 0 or 1

def PrintMatrix(matrix,m,n):
    #The matrix is stored in format as a set of rows. So we print the rows one by one
    for i in range(0,m):
        for j in range(0,n):
            print(str(matrix[i][j])+"  ",end="")
        print("")

def Classify(train_set ,label_set, m, n):
    pass

def MakeRandMatrix(m,n,a,b):
    # here order of matrix is m*n and range of the elements is a to b (both inclusive)
    matrix = []

    #loop to append a row:
    for i in range(0,m):
        #loop to make a row:
        row = []
        for j in range(0,n):
            row.append(randint(a,b))

        matrix.append(row)

    return matrix

matrix = MakeRandMatrix(2,2,1,10)
print(matrix)
PrintMatrix(matrix,2,2)