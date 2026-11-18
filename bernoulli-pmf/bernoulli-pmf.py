import numpy as np
    

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    # Write code here
    x=np.asarray(x,dtype=float)
    size=int(x.size)
    t=np.ones(size)
    dict={
        "pmf":t,
        "mean": 12,
        "variance":12
    }
    dict["mean"]=float(p)
    dict["variance"]=float(p*(1-p))
    pmf=np.where(x==1,p,np.where(x==0,1-p,0.0))
    dict["pmf"]=pmf

    return dict
    


    