import numpy as np
import pandas as pd
from random import randint


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

print(pd.DataFrame(MakeRandMatrix(3,3,1,0)))