#!/usr/bin/python3
"""Nqueens solution"""

import sys


def find_all_solutions(row, column):
    current_solutions = [[]]
    for queen_row in range(row):
        current_solutions = place_queen_on_board(queen_row, column,
                                                 current_solutions)
    return current_solutions


def place_queen_on_board(queen_row, board_size, previous_solutions):
    safe_positions = []
    for solution in previous_solutions:
        for x in range(board_size):
            if is_safe_position(queen_row, x, solution):
                safe_positions.append(solution + [x])
    return safe_positions


def is_safe_position(queen_row, x, current_solution):
    if x in current_solution:
        return False
    else:
        return all(abs(current_solution[column] - x) != queen_row - column
                   for column in range(queen_row))


def initialize_board_size():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit():
        board_size = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def solve_n_queens():
    board_size = initialize_board_size()
    solutions = find_all_solutions(board_size, board_size)
    for solution in solutions:
        formatted_solution = []
        for queen_row, queen_column in enumerate(solution):
            formatted_solution.append([queen_row, queen_column])
        print(formatted_solution)


if __name__ == '__main__':
    solve_n_queens()
