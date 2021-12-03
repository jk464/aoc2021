import argparse
from typing import List  # Python 3.8 and earlier


def find_power_consumption(diagnostics: List[str]) -> int:
    """For a given set of diagnostics return the Power Consumption of the Submarine

    Parameters:
      diagnostics (list): Diagnostics report from Submarine

    Returns:
      power_consumption (int): Power Consumption of the Submarine

    """
    diagnostic_reading_length = len(diagnostics[0]) - 1
    total_diagnostic_readings = len(diagnostics)

    gamma_rate = 0b0
    epsilon_rate = 0b0

    for i in range(diagnostic_reading_length):
        # Bit shift Gamma and Epsilon Rates
        gamma_rate = gamma_rate * 0b10
        epsilon_rate = epsilon_rate * 0b10

        # Find the number of 1 bits by adding up all the bits in the column
        one_count = sum([int(measurement[i]) for measurement in diagnostics])

        # If the count is more than half the total diagnostics, its the most significant
        # Therefore add 1 to Gamma rate, otherwise at one to the Epsilon Rate
        if one_count > total_diagnostic_readings / 2:
            gamma_rate = gamma_rate + 0b1
        else:
            epsilon_rate = epsilon_rate + 0b1

    return int(gamma_rate * epsilon_rate)


def find_rating(ratings: List[str], rating_type: str) -> int:
    """Finds the rating for a given type from a given list of ratings

    Parameters:

      ratings (list): List of binary ratings to find the rating from
      rating_type (str): Either "oxygen" or "c02"

    Returns:

      rating (int): The determined rating for the type.
    """

    rating_length = len(ratings[0]) - 1

    for i in range(rating_length):
        # Find the number of 1 bits by adding up all the bits in the column
        count = sum([int(measurement[i]) for measurement in ratings])

        if rating_type == "oxygen":
            if count >= round(len(ratings) / 2):
                remove_bit = 0
            else:
                remove_bit = 1
        elif rating_type == "C02":
            if count < round(len(ratings) / 2):
                remove_bit = 0
            else:
                remove_bit = 1

        trimmed_list = []

        for measurement in ratings:
            if int(measurement[i]) != remove_bit:
                trimmed_list.append(measurement)

        ratings = trimmed_list.copy()

        if len(ratings) == 1:
            return int(ratings[0], 2)


def find_life_support_rating(diagnostics: List[str]) -> int:
    """For a given set of diagnostics return the Life Support rating of the Submarine

    Parameters:
      diagnostics (list): Diagnostics report from Submarine

    Returns:
      life_support_rating (int): Life Support rating of the Submarine

    """

    oxygen_generator_rating = find_rating(diagnostics.copy(), "oxygen")
    C02_scrubber_rating = find_rating(diagnostics.copy(), "C02")

    return oxygen_generator_rating * C02_scrubber_rating


# Only run if called from the command line
if __name__ == "__main__":

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", help="Inputs file with measurement values")
    args = parser.parse_args()

    # Read in inputs file - also ensure we store values as ints
    with open(args.inputs, "r") as file:
        inputs = file.readlines()

    # Find our answer :)
    print(f"Power Consumption: {find_power_consumption(inputs)}")
    print(f"Life Support Reading: {find_life_support_rating(inputs)}")
