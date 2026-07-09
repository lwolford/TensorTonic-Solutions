def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here

    # This works, but just for fun I want to do this recursively
    """x = x0
    for i in range(steps):
        deriv = (2 * a * x) + b
        x = x - 0.1 * deriv
    return x"""

    if steps == 0:
        return x0

    deriv = (2 * a * x0) + b
    x = x0 - lr * deriv

    return gradient_descent_quadratic(
        a,
        b,
        c,
        x,
        lr,
        steps - 1
    )