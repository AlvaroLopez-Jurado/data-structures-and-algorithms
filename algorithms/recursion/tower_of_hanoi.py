def tower_of_hanoi(n, source, target, auxiliary, moves=None):
    """Resuelve la Torre de Hanoi y devuelve una lista de movimientos."""
    if moves is None:
        moves = []
    if n == 1:
        moves.append((source, target))
    else:
        tower_of_hanoi(n - 1, source, auxiliary, target, moves)
        moves.append((source, target))
        tower_of_hanoi(n - 1, auxiliary, target, source, moves)
    return moves