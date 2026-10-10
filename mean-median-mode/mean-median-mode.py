from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    res = {}
    v = np.asarray(x)

    mean = np.mean(v)
    median = np.median(v)
    res["mean"] = float(mean)
    res["median"] = float(median)

    freq_map = Counter(v)
    sorted_map = sorted(freq_map.items(), key=lambda x : x[1], reverse=True)

    mode = sorted_map[0][0]
    res["mode"] = float(mode)

    return res
        
    
    