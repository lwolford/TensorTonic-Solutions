import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    trace_value = 0
    for idx, each_row in enumerate(A):
        trace_value += each_row[idx]

    return trace_value
        
