import argparse
from PIL import Image

from pixopera.services.math import divisors_list, create_matrix
from pixopera.services.colors import assign_random

def main():
    parser = argparse.ArgumentParser(
        description="You got a favourite image? import it in pixopera and produce your pixelart version of it! Have fun making it more or less precise and let me know if you like it."
    )
    parser.add_argument("--height", type=str, help="Image width")
    parser.add_argument("--width", type=str, help="Image lenght")
    # parser.add_argument("--level", type=float, help="Level of details. This will increase or decrease the number of time used for the image")
    args = parser.parse_args()

    # default values
    height = 100
    width = 400

    if args.height:
        print(f"Option provided: {args.height}")
        height = args.height
    if args.width:
        print(f"Option provided: {args.width}")
        width = args.width

    # level will be the number of dividend of the minimum of the two dimensions.
    # Its the number of time the image will be divided and so the precision of the pixelart
    level = 100

    print("Hello, Pixopera!")
    min_block_dimension = get_min_block_dimension(height, width, level)
    print(f"min_block_dimension: {min_block_dimension}")
    matrix = create_matrix(height, width, min_block_dimension)
    assign_random(matrix)
    # print(matrix)
    print_image(matrix, min_block_dimension)


def get_min_block_dimension(height, width, level):
    divisors = divisors_list(height, width)
    print(f"divisors: {divisors}")
    selected = int(len(divisors) * (level / 100) - 1)
    print(f"selected: {selected}")
    return divisors[selected]


def print_image(matrix, min_block_dimension):
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0 

    # Initialize a new image with a size of (width, height)
    image = Image.new("RGB", (cols * min_block_dimension, rows * min_block_dimension))

    # Iterate over the matrix and set pixels
    for i in range(rows):
        for j in range(cols):
            # Extract the color (second element of the tuple)
            color = matrix[i][j][1]  
            for x in range(min_block_dimension):
                for y in range(min_block_dimension):
                    # Set the color for each pixel in the block
                    image.putpixel(
                        (j * min_block_dimension + x, i * min_block_dimension + y),
                        color,
                    )
    # Show or save the image
    image.show()


if __name__ == "__main__":
    main()
