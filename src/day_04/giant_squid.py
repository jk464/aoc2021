import argparse
from typing import List, Tuple  # Python 3.8 and earlier
from pprint import pprint


def check_bingo_board(
    board: List[List[int]], drawn_numbers: List[int]
) -> Tuple[int, int]:

    board_winning_draw = None

    # Check Rows
    for row in board:
        line_winning_draw = None
        for entry in row:
            matching_draw = drawn_numbers.index(entry)

            if matching_draw == -1:
                line_winning_draw = None
                break
            elif line_winning_draw is None or matching_draw > line_winning_draw:
                line_winning_draw = matching_draw

        if (
            line_winning_draw
            and board_winning_draw is None
            or line_winning_draw < board_winning_draw
        ):
            board_winning_draw = line_winning_draw

    # Check columns
    for column in range(len(board[0])):
        line_winning_draw = None
        for row in board:
            matching_draw = drawn_numbers.index(row[column])

            if matching_draw == -1:
                line_winning_draw = None
                break
            elif line_winning_draw is None or matching_draw > line_winning_draw:
                line_winning_draw = matching_draw

        if (
            line_winning_draw
            and board_winning_draw is None
            or line_winning_draw < board_winning_draw
        ):
            board_winning_draw = line_winning_draw

    return (
        sum(
            [
                sum(
                    [
                        entry
                        for entry in row
                        if not drawn_numbers.index(entry) <= board_winning_draw
                    ]
                )
                for row in board
            ]
        )
        * drawn_numbers[board_winning_draw],
        board_winning_draw,
    )


def find_best_board(boards: List[List[List[int]]], drawn_numbers: List[int]) -> int:
    board_winning_draw = None

    for board in boards:
        board_result = check_bingo_board(board, drawn_numbers)

        if board_winning_draw is None or board_result[1] < board_winning_draw[1]:
            board_winning_draw = board_result

    return board_winning_draw[0]


def find_worst_board(boards: List[List[List[int]]], drawn_numbers: List[int]) -> int:
    board_winning_draw = None

    for board in boards:
        board_result = check_bingo_board(board, drawn_numbers)

        if board_winning_draw is None or board_result[1] > board_winning_draw[1]:
            board_winning_draw = board_result

    return board_winning_draw[0]


# Only run if called from the command line
if __name__ == "__main__":
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", help="Inputs file with values")

    args = parser.parse_args()

    # Read in inputs file - also ensure we store values as ints
    with open(args.inputs, "r") as file:
        lines = file.readlines()
        drawn_numbers = [int(i) for i in lines[0].split(",")]

        boards = []
        board = []
        for line in lines[2:]:
            if line == "\n":
                boards.append(board.copy())
                board = []
            else:
                board.append([int(i) for i in line.split(" ") if i != ""])

        boards.append(board.copy())

    # Find our answer :)
    print(find_best_board(boards, drawn_numbers))
    print(find_worst_board(boards, drawn_numbers))
