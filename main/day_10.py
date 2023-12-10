from main.file_reader import read
import sys

sys.setrecursionlimit(100000)


def solve_1(input: list) -> int:
    start = find_start(input)

    coords_in_loop = set()
    dfs(start, input, coords_in_loop, 0)

    return len(coords_in_loop) // 2


def find_start(input):
    for row, row_val in enumerate(input):
        for col, val in enumerate(row_val):
            if val == "S":
                start = (row, col)
    return start


def dfs(
    current_point,
    input,
    coords_in_loop,
    steps,
):
    max_row, max_col = len(input), len(input[0])
    if current_point not in coords_in_loop:
        coords_in_loop.add(current_point)
        curr_type = input[current_point[0]][current_point[1]]
        adjacent_coords = get_adjacent_coords(
            curr_type, current_point, max_row, max_col, input
        )
        for a_row, a_col in adjacent_coords:
            dfs(
                (a_row, a_col),
                input,
                coords_in_loop,
                steps + 1,
            )


def get_adjacent_coords(curr_type, point, max_row, max_col, input):
    row, col = point
    adjacent_coords = []
    if (
        row > 0
        and curr_type in {"|", "L", "J", "S"}
        and input[row - 1][col] in {"|", "7", "F"}
    ):
        adjacent_coords.append((row - 1, col))
    if (
        row < max_row - 1
        and curr_type in {"|", "F", "7", "S"}
        and input[row + 1][col] in {"|", "L", "J"}
    ):
        adjacent_coords.append((row + 1, col))
    if (
        col > 0
        and curr_type in {"-", "J", "7", "S"}
        and input[row][col - 1] in {"-", "L", "F"}
    ):
        adjacent_coords.append((row, col - 1))
    if (
        col < max_col - 1
        and curr_type in {"-", "L", "F", "S"}
        and input[row][col + 1] in {"-", "J", "7"}
    ):
        adjacent_coords.append((row, col + 1))
    return adjacent_coords


def solve_2(input: list) -> int:
    start = find_start(input)

    coords_in_loop = set()

    dfs(start, input, coords_in_loop, 0)

    num_inside = 0
    for row in range(len(input)):
        is_inside = False
        for col in range(len(input[0])):
            c = input[row][col]
            if (row, col) in coords_in_loop and c in {"|", "L", "J"}:
                is_inside = not is_inside
            if (row, col) not in coords_in_loop and is_inside:
                num_inside += 1

    return num_inside


if __name__ == "__main__":
    input = read("day10-01.txt")
    print(solve_1(input))  # 6864
    print(solve_2(input))  # 349
