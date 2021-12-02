import argparse
from typing import List  # Python 3.8 and earlier


def calculate_moved_distance(movements: list, use_aim: bool = False) -> int:
    """For a given set of movement inputs calculates the horizontal and vertical distance moved and returns the product of the two values

    Parameteres:
      movements (list): List of movement inputs - Each list entry, is a pair of [movement direction, movement value]
      use_aim (bool): Define whether up / down movements indicated a change in depth or aim.

    Returns
      movement_product (int): Product of the horizontal and vertical distance moved
    """

    x = 0
    y = 0
    aim = 0

    for move in movements:
        if move[0] == "forward":
            x += move[1]
            if use_aim:
                y += move[1] * aim
        elif move[0] == "down":
            if use_aim:
                aim += move[1]
            else:
                y += move[1]
        elif move[0] == "up":
            if use_aim:
                aim -= move[1]
            else:
                y -= move[1]

    movement_product = x * y

    return movement_product


# Only run if called from the command line
if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", help="Inputs file with values")
    parser.add_argument('--aim', action='store_true', default=False)

    args = parser.parse_args()

    # Read in inputs file - also ensure we store values as ints
    with open(args.inputs, "r") as file:
        inputs = [[l.split(" ")[0], int(l.split(" ")[1])] for l in file.readlines()]

    # Find our answer :)
    print(calculate_moved_distance(inputs, args.aim))
