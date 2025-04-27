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

def Classify(train_set ,label_set, m, n):
    # Decision tree matrix format:
    # [.......]
    # one element -> "p{'GE'or'LE}qr" where p -> index of the feature
                                            # q -> value
                                            # r -> label
    # if the if statement is true then r label is returned or else we go to the next if statement
    # if none satisfied we will return 2 for debugging

    des_tree = []
    matrix=train_set
    labels=label_set

    while True:
        #we break when the whole matrix is labelled the same

        #how to check if all the elements of an array are identical
        for i in des_tree:
            if(labels[1]!=labels[i]):
                break

        for i in range(0,n):
            # finding the lower and upper limits in ith feature
            LL = matrix[0][i]
            UL = matrix[0][i]
            for a in range(0,len(matrix)):
                if(matrix[a][i]>UL):
                    matrix[a][i] = UL
            for a in range(0,len(matrix)):
                if(matrix[a][i]<LL):
                    matrix[a][i] = LL

            #Now we go from 
