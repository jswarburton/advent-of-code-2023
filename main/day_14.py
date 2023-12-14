from main.file_reader import read


def solve_1(input: list) -> int:
    tilt_north(input)

    total = 0
    for row_num, row in enumerate(input):
        for col_num, col in enumerate(row):
            if col == "O":
                total += len(input) - row_num

    return total


def solve_2(input: list) -> int:
    seen = dict()

    i = 0

    while i < 1000000000:
        stringified_grid = str(input)

        if stringified_grid in seen:
            last_index = seen[stringified_grid]

            cadence = i - last_index

            i += ((1000000000 - i) // cadence) * cadence
        else:
            seen[stringified_grid] = i

        # NORTH
        tilt_north(input)

        # WEST
        input = rotate_clockwise(input)
        tilt_north(input)

        # SOUTH
        input = rotate_clockwise(input)
        tilt_north(input)

        # EAST
        input = rotate_clockwise(input)
        tilt_north(input)

        input = rotate_clockwise(input)

        i += 1

    total = 0

    for row_num, row in enumerate(input):
        for col_num, col in enumerate(row):
            if col == "O":
                total += len(input) - row_num

    return total


def tilt_north(input):
    for row_num, row in enumerate(input):
        for col_num, col in enumerate(row):
            if col == "O":
                new_row = find_furthest_north_possible(row_num, col_num, input)
                if new_row != row_num:
                    input[new_row] = (
                        input[new_row][:col_num] + "O" + input[new_row][col_num + 1 :]
                    )
                    input[row_num] = (
                        input[row_num][:col_num] + "." + input[row_num][col_num + 1 :]
                    )


def rotate_clockwise(grid):
    rows = len(grid)
    cols = len(grid[0])

    rotated_grid = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated_grid[j][rows - 1 - i] = grid[i][j]

    return ["".join(r) for r in rotated_grid]


def find_furthest_north_possible(row_num, col_num, input):
    curr_row_num = row_num
    for i in reversed(range(row_num)):
        if input[i][col_num] in "#O":
            return curr_row_num
        else:
            curr_row_num -= 1
    return curr_row_num


if __name__ == "__main__":
    input = read("day14-01.txt")
    print(solve_1(input))  # 106648
    print(solve_2(input))  # 87700
