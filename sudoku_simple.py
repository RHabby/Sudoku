# Простейшая реализация алгоритма решения судоку

backtracks = 0


# Функция производит проверку клетки на заполненность значением
def is_empty(grid: list) -> tuple:
    # Поиск незаполненной клетки на доске
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                return x, y
    return -1, -1


def is_valid(grid: list, i: int, j: int, number: int) -> bool:
    is_row_ok = all([number != grid[i][x] for x in range(9)])

    if is_row_ok:
        is_column_ok = all([number != grid[x][j] for x in range(9)])

        if is_column_ok:
            top_sec_x, top_sec_y = (i // 3) * 3, (j // 3) * 3

            for x in range(top_sec_x, top_sec_x + 3):
                for y in range(top_sec_y, top_sec_y + 3):
                    if grid[x][y] == number:
                        return False

            return True

    return False


def solver(grid: list, i: int = 0, j: int = 0) -> bool:
    global backtracks

    i, j = is_empty(grid)
    if i == -1:
        return True

    for number in range(1, 9 + 1):
        if is_valid(grid, i, j, number):
            grid[i][j] = number
            if solver(grid, i, j):
                return True

        backtracks += 1
        grid[i][j] = 0

    return False


def print_sudoku(grid: list):
    row_number = 0
    for row in grid:
        if row_number % 3 == 0 and row_number != 0:
            print(" ")
        print(f"{row[:3]} {row[3:6]} {row[6:]}")
        row_number += 1


if __name__ == "__main__":
    expert_grid = [
        [9, 1, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 7, 0, 1, 3, 0, 0, 8],
        [6, 0, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 0, 0, 7, 3, 4],
        [0, 0, 0, 5, 0, 0, 0, 1, 0],
        [3, 4, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 9, 0, 6],
        [0, 0, 0, 8, 0, 0, 0, 7, 0]
    ]

    backtracks = 0
    print("Base Grid:")
    print_sudoku(expert_grid)
    print("-" * 35)
    print(f"Solved: {solver(expert_grid)}")
    print("Solved Grid:")
    print_sudoku(expert_grid)
    print(f"Backtracks: {backtracks}")
    print("-" * 35)
    print("Done!")
