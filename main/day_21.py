from main.file_reader import read


def solve_1(input: list, steps: int) -> int:
    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] == "S":
                start_pos = (row, col)

    visited = set()
    visited.add(start_pos)

    for i in range(steps):
        new_visited = set()
        for x, y in list(visited):
            neighbours = get_neighbours(x, y, input)
            for neighbor in neighbours:
                new_visited.add(neighbor)
        visited = new_visited
    return len(visited)


def get_neighbours(x: int, y: int, input: list) -> list:
    DIRS = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0),
    ]
    neighbors = []
    for dir in DIRS:
        new_x = x + dir[0]
        new_y = y + dir[1]
        if (
            0 <= new_x < len(input)
            and 0 <= new_y < len(input[0])
            and input[new_x][new_y] != "#"
        ):
            neighbors.append((new_x, new_y))

    return neighbors


if __name__ == "__main__":
    input = read("day21-01.txt")
    print(solve_1(input, steps=64))  # 3773
