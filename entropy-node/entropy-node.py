import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    class_index, class_count = np.unique(y, return_counts=True)
    class_p = class_count / np.sum(class_count)
    entropy = -np.sum(class_p * np.log2(class_p))
    
    return entropy