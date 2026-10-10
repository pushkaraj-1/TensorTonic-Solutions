import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    v = np.asarray(x)
    mean = float(np.mean(v))
    sqrd = 0.0
    for i in range(len(x)):
        sqrd += float(np.square(x[i] - mean))

    variance = float(sqrd / (len(x) - 1))
    standard_deviation = float(np.sqrt(variance))
    res = {}
    res["variance"] = variance
    res["standard_deviation"] = standard_deviation
    
    return res
        