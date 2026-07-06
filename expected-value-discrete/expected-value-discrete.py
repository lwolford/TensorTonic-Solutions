import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    if not np.allclose(np.sum(p), [1]):
        raise ValueError
    
    return np.sum(np.multiply(x, p))
