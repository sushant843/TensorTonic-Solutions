import torch

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Returns the scaled dot-product attention output.
    """
    
    D_K =K.shape[-1]
    Simi=Q @ K.transpose(-2,-1)
    Simi_scaled=Simi/(D_K**0.5)
    Attention_wt=torch.softmax(Simi_scaled, dim=-1)
    Out=Attention_wt @ V
    return Out
    