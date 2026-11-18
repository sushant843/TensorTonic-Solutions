import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    X=np.asarray(x)
    Y=np.asarray(y)
    result=np.dot(X,Y)
    result=float(result)
    return result
   