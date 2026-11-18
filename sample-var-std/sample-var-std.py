import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    dict={
        "variance":3 ,
        "standard_deviation":5
    }
    dict["variance"]=float(np.var(x,axis=0,ddof=1))
    dict["standard_deviation"]=float((float(np.var(x,axis=0,ddof=1)))**0.5)
    return dict
    