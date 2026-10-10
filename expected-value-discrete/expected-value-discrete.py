import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    x_vec = np.asarray(x)
    p_vec = np.asarray(p)
    res = 0.0
    for i in range(len(x)):
        res += float(x_vec[i]*p_vec[i])

    return res