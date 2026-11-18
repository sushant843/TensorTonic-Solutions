import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    A=np.asarray(A)
    dim=A.ndim
    if (dim==1): return A.reshape(-1,1)
        
    else: return A.T
        
    
   
