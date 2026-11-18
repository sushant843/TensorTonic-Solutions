from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    dict={
        "mean":12,
        "median":12,
        "mode":12
    }
    x=np.asarray(x,dtype=float)
    dict["mean"]=float(np.mean(x,axis=0))
    dict["median"]=float(np.median(x,axis=0))
    val,count=np.unique(x,return_counts=True)
    dict["mode"]=float(val[np.argmax(count)])

    return dict