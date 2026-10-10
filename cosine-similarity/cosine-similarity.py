import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    mod_a = np.linalg.norm(a) 
    mod_b = np.linalg.norm(b) 
    if mod_a == 0 or mod_b == 0:
        return 0.0

    v1 = np.asarray(a)
    v2 = np.asarray(b)
    return float(np.dot(v1,v2) / (mod_a*mod_b))