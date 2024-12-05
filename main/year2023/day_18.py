from main.file_reader import read


def solve_1(input: list) -> int:
    dirs_and_dists = [
        (dir, int(dist)) for dir, dist, _ in (i.split(" ") for i in input)
    ]
    return solve(dirs_and_dists)


def solve_2(input: list) -> int:
    dirs_and_dists = []
    for i in input:
        _, _, color_code = i.split(" ")

        actual_code = color_code.split("(#")[1].split(")")[0]

        dist = int(actual_code[:5], 16)
        dir = int(actual_code[-1])

        if dir == 3:  # "U"
            dir = "U"
        elif dir == 1:  # "D"
            dir = "D"
        elif dir == 0:  # "R"
            dir = "R"
        elif dir == 2:  # "L"
            dir = "L"

        dirs_and_dists.append((dir, dist))

    return solve(dirs_and_dists)


def solve(dirs_and_dists):
    pos = (0, 0)
    points = [pos]
    border_length = 0
    for dir, dist in dirs_and_dists:
        if dir == "U":
            pos = (pos[0] - dist, pos[1])
        elif dir == "D":
            pos = (pos[0] + dist, pos[1])
        elif dir == "R":
            pos = (pos[0], pos[1] + dist)
        elif dir == "L":
            pos = (pos[0], pos[1] - dist)

        border_length += dist
        points.append(pos)

    # Shoelace formula
    points = points[::-1]
    area = 0
    for i in range(len(points) - 1):
        area += (points[i][1] + points[i + 1][1]) * (points[i][0] - points[i + 1][0])
    area = abs(area) // 2

    # Pick's formula: area = points_inside_polygon + border_length/2 - 1
    points_inside_polygon = area - border_length // 2 + 1

    return points_inside_polygon + border_length


if __name__ == "__main__":
    input = read("day18-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 56678
    print(solve_2(input))  # 79088855654037
