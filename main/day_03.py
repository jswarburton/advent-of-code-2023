from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0

    for x in range(len(input)):
        neighbours = []
        num = ""
        for y in range(len(input[0])):
            if not input[x][y].isdigit():
                for n1, n2 in neighbours:
                    n = input[n1][n2]

                    if not n.isdigit() and not n == ".":
                        total += int(num)
                        break

                num = ""
                neighbours = []
            else:
                num += input[x][y]
                neighbours.extend(get_neighbours(x, y, input))
        for n1, n2 in neighbours:
            n = input[n1][n2]

            if not n.isdigit() and not n == ".":
                total += int(num)
                break

    return total


def get_neighbours(x: int, y: int, input: list) -> list:
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue
            if 0 <= x + i < len(input) and 0 <= y + j < len(input[0]):
                if not (i == 0 and input[x + i][y + j].isdigit()):
                    neighbors.append((x + i, y + j))
    return neighbors


def solve_2(input: list) -> int:
    gears = dict()

    total = 0

    for x in range(len(input)):
        neighbours = []
        num = ""
        for y in range(len(input[0])):
            if not input[x][y].isdigit():
                for n1, n2 in neighbours:
                    n = input[n1][n2]

                    if not n.isdigit() and not n == ".":
                        if n == "*":
                            if (n1, n2) in gears:
                                gears[(n1, n2)].append(int(num))
                            else:
                                gears[(n1, n2)] = [int(num)]
                        break

                num = ""
                neighbours = []
            else:
                num += input[x][y]
                neighbours.extend(get_neighbours(x, y, input))

        for n1, n2 in neighbours:
            n = input[n1][n2]

            if n == "*":
                if (n1, n2) in gears:
                    gears[(n1, n2)].append(int(num))
                else:
                    gears[(n1, n2)] = [int(num)]

            if not n.isdigit() and not n == ".":
                break

    for x in gears.keys():
        if len(gears[x]) == 2:
            total += gears[x][0] * gears[x][1]

    return total


if __name__ == "__main__":
    input = read("day03-01.txt")
    print(solve_1(input))  # 530849
    print(solve_2(input))  # 84900879
