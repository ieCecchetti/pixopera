def divisors_list(v1, v2):
    """Return a list of all the divisors of the two numbers.

    Args:
        v1 (int): first value to be divided
        v2 (int): second value to be divided

    Returns:
        list: list of all the divisors of the two numbers
    """
    divs = []
    for i in range(1, min(v1, v2) + 1):
        if v1 % i == 0 and v2 % i == 0:
            divs.append(i)
    return divs

def create_matrix(height, width, min_block_dimension):
    """Create a matrix of the image.

    Args:
        height (int): height of the image
        width (int): width of the image
        min_block_dimension (int): minimum block dimension

    Returns:
        list: matrix of the image
    """
    matrix = []
    for i in range(0, height, min_block_dimension):
        row = []
        for j in range(0, width, min_block_dimension):
            row.append(((i, j), 0))
        matrix.append(row)
    return matrix
