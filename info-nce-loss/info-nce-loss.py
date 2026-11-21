import numpy as np

def info_nce_loss(Z1: list, Z2: list, temperature: float = 0.1) -> float:
    """
    Returns the loss as a float.
    """
    Z1=np.asarray(Z1,dtype=float)
    Z2=np.asarray(Z2,dtype=float)
    similarity=Z1@Z2.T/temperature
    shift=similarity-np.max(similarity,axis=1,keepdims=True)
    log_denominator=np.log(np.sum(np.exp(shift),axis=1))
    loss=-np.diag(shift)+log_denominator
    return float(np.mean(loss))
    