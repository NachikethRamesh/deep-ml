import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    if len(a[0]) != len(b):
        return -1

    c = []

    for vecA in a:
        vecOut = []
        for vecB in np.array(b).T:
            vecB = vecB.tolist()
            prod = 0
            for i, j in zip(vecA, vecB):
                prod += i * j

            vecOut.append(prod)
        c.append(vecOut)
    
    return c







    return c