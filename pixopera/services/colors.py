import random


def generate_random_color():
    """Generate a random RGB color.

    Returns:
        tuple: A tuple representing the RGB color.
    """
    # Generate random values for R, G, B channels in the range 0-255
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def assign_random(matrix):
    """Assign a random color to each block of the matrix.

    Args:
        matrix (list): matrix of the image
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Update the second element (color) of the tuple with a random color
            matrix[i][j] = (matrix[i][j][0], generate_random_color())
