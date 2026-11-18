import math
def pmf_at_k(n,p,k):
    return ((p**k)*((1-p)**(n-k)))*math.comb(n,k)
def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    output={
        "pmf":0.24,
        "cdf":0.45
    }
    output["pmf"]=float(pmf_at_k(n,p,k))
    sum=0
    for i in range(k+1):
        sum+=float(pmf_at_k(n,p,i))
    output["cdf"]=sum
    return output