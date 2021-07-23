import numpy as np
from numpy.lib.function_base import insert

def find_outliers(data):
    outliers = []
    threshold = 2
    mean = np.mean(data)
    print("mean: ",mean)
    sd = np.std(data)
    print("standard deviation: ",sd)
    for i in data:
        z_score = (i-mean)/sd
        if np.abs(z_score)>threshold:
            outliers.append(i)
    print("\nThe outliers in the given data are: ",outliers)    


# data is given here in the form of list
gvn_data = [8, 17, 15, -99, 2, 1, -4, -9, -5, 3, 88, -7,]
print("The given data is: ",gvn_data)
find_outliers(gvn_data)
