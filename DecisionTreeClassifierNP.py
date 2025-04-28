import numpy as np
import pandas as pd
from matrixUtils import *

data = pd.DataFrame(MakeRandMatrix(20,4,0,20))
labels = pd.DataFrame(MakeRandMatrix(20,1,0,1))
    

print(data.head())