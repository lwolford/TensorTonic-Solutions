import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # So you can definitely do np.transpose(A), but I'll actually implement it
    rows = len(A)
    columns = len(A[0])

    new_columns = []
    for i in range(columns):
        new_rows = []
        for j in range(rows):
            new_rows.append(A[j][i])
        new_columns.append(new_rows)
    
    return np.matrix(new_columns)