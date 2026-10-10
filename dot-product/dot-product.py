import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    x_vector = np.asarray(x, dtype=float)
    y_vector = np.asarray(y, dtype=float)

    res = np.dot(x_vector, y_vector)
    return float(res)
    