from math import comb


def lattice_paths(rows: int, movements: int) -> int:
    """
    Calculate the number of unique lattice paths from start to end point.

    Given a grid with specified number of rows and allowed movements, calculates
    the total number of possible unique paths using combinations formula.

    Args:
        rows (int): Number of rows in the grid
        movements (int): Number of allowed movements

    Returns:
        int: Total number of unique lattice paths

    Example:
        >>> lattice_paths(2, 2)
        6
    """
    return comb(rows + movements, rows)
