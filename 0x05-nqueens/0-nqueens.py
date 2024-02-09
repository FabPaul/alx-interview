#!/usr/bin/python3
"""Nqueens solution"""

import sys


def is_queen(board, row, col, n):
    """Checks if it's safe to place queen at a given position on the board"""
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, n):
    """Recursively solve the N queens"""
    # If all queens are placed, print the positions of the queens
    if row == n:
        queens_positions = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    queens_positions.append([i, j])
        print(queens_positions)
        return True

    re = False
    # Place a queen in each column of the current row
    for col in range(n):
        if is_queen(board, row, col, n):
            board[row][col] = 1
            re = solve_nqueens_util(board, row + 1, n) or re
            board[row][col] = 0

    return re


def n_queens(n):
    """Solve the nqueen and print all possible solutions"""

    if n < 4:
        print("N must be at leaset 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]

    if not solve_nqueens_util(board, 0, n):
        print("No solution exists")
    return


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if N is a number
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    n_queens(N)
