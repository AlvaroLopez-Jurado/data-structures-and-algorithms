def factorial(n):
    """Calcula el factorial de un número de forma recursiva."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)