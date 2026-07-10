def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    h_out = ((len(X) - pool_size) // stride) + 1
    w_out = ((len(X[0]) - pool_size) // stride) + 1

    matrix = []
    for i in range(h_out):
        row_list = []
        for j in range(w_out):
            pool_list = []
            for a in range(pool_size):
                for b in range(pool_size):
                    pool_list.append(
                        X[i * stride + a][j * stride + b]
                    )
            row_list.append(max(pool_list))
        matrix.append(row_list)

    return matrix
            