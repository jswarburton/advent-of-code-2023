from main.file_reader import read


def solve_1(input: list) -> int:
    return solve((0, 0), "right", input)


def solve_2(input: list) -> int:
    starting_points = set()

    for col in range(len(input[0])):
        starting_points.add(((0, col), "down"))
        starting_points.add(((len(input) - 1, col), "up"))

    for row in range(len(input)):
        starting_points.add(((row, 0), "right"))
        starting_points.add(((row, len(input[0]) - 1), "left"))

    max_num_energized = 0

    for (row, col), dir in starting_points:
        num_energized = solve((row, col), dir, input)
        if num_energized > max_num_energized:
            max_num_energized = num_energized

    return max_num_energized


def solve(start: tuple, dir: str, input: list) -> int:
    points = [(start, dir)]

    curr_energised = set()

    while not all(p in curr_energised for p in points):
        new_points = []

        points_not_covered = [p for p in points if p not in curr_energised]

        for (row, col), dir in points_not_covered:
            dirs = []

            if input[row][col] == "|":
                if dir == "right" or dir == "left":
                    dirs = ["up", "down"]
                else:
                    dirs = [dir]
            elif input[row][col] == "-":
                if dir == "up" or dir == "down":
                    dirs = ["left", "right"]
                else:
                    dirs = [dir]
            elif input[row][col] == ".":
                dirs = [dir]
            elif input[row][col] == "\\":
                if dir == "right":
                    dirs = ["down"]
                elif dir == "left":
                    dirs = ["up"]
                elif dir == "up":
                    dirs = ["left"]
                elif dir == "down":
                    dirs = ["right"]
            elif input[row][col] == "/":
                if dir == "right":
                    dirs = ["up"]
                elif dir == "left":
                    dirs = ["down"]
                elif dir == "up":
                    dirs = ["right"]
                elif dir == "down":
                    dirs = ["left"]

            for d in dirs:
                if d == "right" and col + 1 < len(input[row]):
                    new_points.append(((row, col + 1), d))
                elif d == "left" and col - 1 >= 0:
                    new_points.append(((row, col - 1), d))
                elif d == "up" and row - 1 >= 0:
                    new_points.append(((row - 1, col), d))
                elif d == "down" and row + 1 < len(input):
                    new_points.append(((row + 1, col), d))

        for p in points:
            curr_energised.add(p)
        points = new_points

    return len(set(c[0] for c in curr_energised))


if __name__ == "__main__":
    input = read("day16-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 7517
    print(solve_2(input))  # 7741
