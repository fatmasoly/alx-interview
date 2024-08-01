#!/usr/bin/python3
""" N queens problem """

import sys


def print_usage():
    """ Print the usage """
    print("Usage: nqueens N")


def print_error(message):
    """ Print an error message """
    print(message)


def is_valid(board, row, col):
    """ Check if a queen can be placed on board[row][col] """
    for i in range(row):
        if board[i] == col:
            return False
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N, row, board, solutions):
    """ Solve the N queens problem """
    if row == N:
        solutions.append(board[:])
        return
    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1


def print_solutions(solutions):
    """ Print the solutions """
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


def main():
    """ Main function """
    if len(sys.argv) != 2:
        print_usage()
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_error("N must be a number")
        sys.exit(1)

    if N < 4:
        print_error("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
