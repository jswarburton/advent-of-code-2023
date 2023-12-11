from main.file_reader import read


def solve_1(input: list) -> int:
    return solve(input)


def solve_2(input: list) -> int:
    return solve(input, 1000000)


def combinations(input: list) -> set:
    return {(x, y) for x in input for y in input if x < y}


def manhattan_distance(a: tuple, b: tuple) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve(input: list, multiplier=2) -> int:
    empty_rows = {
        row_num for row_num, row in enumerate(input) if all(char == "." for char in row)
    }

    empty_cols = {
        col_num
        for col_num in range(len(input[0]))
        if all(row[col_num] == "." for row in input)
    }

    locations = [
        (row, col)
        for row in range(len(input))
        for col in range(len(input[0]))
        if input[row][col] == "#"
    ]

    total_distance = 0
    for (r1, c1), (r2, c2) in combinations(locations):
        row_add = 0
        for empty_row in empty_rows:
            if r1 < empty_row < r2 or r2 < empty_row < r1:
                row_add += 1
        col_add = 0
        for empty_col in empty_cols:
            if c1 < empty_col < c2 or c2 < empty_col < c1:
                col_add += 1

        total_distance += (
            manhattan_distance((r1, c1), (r2, c2))
            + ((multiplier - 1) * row_add)
            + ((multiplier - 1) * col_add)
        )

    return total_distance


if __name__ == "__main__":
    input = read("day11-01.txt")
    print(solve_1(input))  # 9957702
    print(solve_2(input))  # 512240933238
