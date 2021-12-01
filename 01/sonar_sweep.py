import argparse


def window_total(measurements, window):
    """Gets the total sum of measurements across an arbitrary range length (window)

    Parameters:
      measurements (list): List of measurements to take values from
      window       (int) : Size of range to sum over

    Returns:
      total (int): Total of the sum over the window
    """

    total = 0

    for i in range(window):
        total += measurements[i]

    return total


def find_increase_count(measurements, window=1):
    """For a given set of measurements and for a give window size, find how many times there's an increase in the sum of consecutive measurements

    Parameters:
      measurements (list): List of measurements to take values from
      window       (int) : Size of range to sum over

    Returns:
      higher_count (int): How many times there's an increase in the sum of consecutive measurements
    """

    previous_measurement = None
    higher_count = 0
    i = 0
    for measurement in measurements[: len(measurements) - window + 1]:
        total = window_total(measurements[i : i + window], window)

        if previous_measurement is not None and total > previous_measurement:
            higher_count += 1

        previous_measurement = total
        i += 1

    return higher_count


# Only run if called from the command line
if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", help="Inputs file with measurement values")
    parser.add_argument(
        "--window",
        help="Size of rolling measurement window, default 1",
        nargs="?",
        const="default",
        default=1,
        type=int,
    )
    args = parser.parse_args()

    # Read in inputs file - also ensure we store values as ints
    with open(args.inputs) as file:
        inputs = []
        for line in file.readlines():
            inputs.append(int(line))

    # Find our answer :)
    print(find_increase_count(inputs, window=args.window))
