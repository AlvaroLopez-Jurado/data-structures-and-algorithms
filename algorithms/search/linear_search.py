def linear_search(arr, target):
    """Realiza una búsqueda lineal de target en arr."""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1