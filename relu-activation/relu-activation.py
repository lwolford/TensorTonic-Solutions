import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    x = np.asarray(x, dtype=float)
    activation = np.maximum(0, x)
    # Write code here
    return activation