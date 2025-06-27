def lcm(a, b):
    """Calcula el mínimo común múltiplo usando el MCD."""
    from algorithms.math.gcd import gcd
    return abs(a * b) // gcd(a, b)