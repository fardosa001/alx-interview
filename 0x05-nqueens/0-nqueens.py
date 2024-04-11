#!/usr/bin/python3
""" solves N queens problem"""
import sys


def is_safe(board, row, col):
    """checks if it is safe to place a queen at a position"""
    for i in range(row):
        # Check if there is a queen in the same column or diagonal
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens_util(board, row, N):
    """tries to find all possible solutions for the N queens problem."""
    if row == N:
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens_util(board, row + 1, N)
            board[row] = -1


def solve_nqueens(N):
    """entry point for solving the N queens problem."""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solve_nqueens_util(board, 0, N)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
