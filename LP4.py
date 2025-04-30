def is_safe(board, row, col):
    n = len(board)

    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check the lower diagonal
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1

    # If no conflicts found, it's safe to place a queen
    return True

def backtrack(board, col, solutions):
    n = len(board)

    # If all queens are placed, a valid solution is found
    if col == n:
        solutions.append([row[:] for row in board])
        return

    # Explore all possible positions in the current column
    for row in range(n):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place a queen
            # Recursively move to the next column
            backtrack(board, col + 1, solutions)
            board[row][col] = 0  # Remove the queen (backtrack)

def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    backtrack(board, 0, solutions)
    return solutions

# Example usage
n = 4
solutions = solve_nqueens(n)
print(f"Total solutions for {n}-queens problem: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        print(row)
    print()