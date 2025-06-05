# Using the determinant method, check whether a given system of equations is consistent or inconsistent

import numpy as np
def chcek(matrix):
    det=np.linalg.det(matrix)
    if(det!=0):
        print("The syste of equation is consistent")
    else:
        print("The system of equation is inconsistent")

matrics1=np.array([[1,3,4],[7,9,2],[2,5,1]])
matrics2=np.array([[2,3,9],[5,9,8],[5,9,7]])
chcek(matrics1)
