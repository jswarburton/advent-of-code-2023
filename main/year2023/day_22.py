from main.file_reader import read


def solve_1(input: list) -> int:
    bricks = parse_and_settle(input)

    # brick ID to bricks it supports
    support_mapping = get_supporting_mapping(bricks)
    being_supported_by = get_being_supported_by(support_mapping)

    total = 0
    for i in bricks.keys():
        for j, v in being_supported_by.items():
            if v == {i}:
                total += 1
                break

    return len(bricks) - total


def get_being_supported_by(support_mapping):
    being_supported_by = dict()
    for i, supportings in support_mapping.items():
        for s in supportings:
            if s in being_supported_by:
                being_supported_by[s].add(i)
            else:
                being_supported_by[s] = {i}
    return being_supported_by


def parse_and_settle(input):
    bricks = []
    for i, line in enumerate(input):
        start, end = line.split("~")
        ax, ay, az = start.split(",")
        bx, by, bz = end.split(",")
        bricks.append((int(ax), int(ay), int(az), int(bx), int(by), int(bz)))
    bricks = settle(bricks)
    bricks = {i: brick for i, brick in enumerate(bricks)}
    return bricks


def points(brick):
    start = brick[0], brick[1], brick[2]
    end = brick[3], brick[4], brick[5]
    pos = []
    for x in range(start[0], end[0] + 1):
        for y in range(start[1], end[1] + 1):
            for z in range(start[2], end[2] + 1):
                pos.append((x, y, z))

    return pos


def settle(bricks):
    sorted_bricks = sorted(bricks, key=lambda b: b[2])

    occupied = dict()
    settled = []

    for brick in sorted_bricks:
        while True:
            next_brick = (
                brick[0],
                brick[1],
                brick[2] - 1,
                brick[3],
                brick[4],
                brick[5] - 1,
            )

            if not any(p in occupied for p in points(next_brick)) and next_brick[2] > 0:
                brick = next_brick
            else:
                for point in points(brick):
                    occupied[point] = brick
                settled.append(brick)
                break

    return settled


def get_supporting_mapping(bricks):
    supporting_mapping = dict()
    for i, brick in bricks.items():
        ps = points(brick)
        ps_above = {(x, y, z + 1) for x, y, z in ps}
        for j, brick2 in bricks.items():
            if i != j:
                ps2 = set(points(brick2))

                if len(ps_above.intersection(ps2)) != 0:
                    curr = supporting_mapping.get(i, set())
                    curr.add(j)
                    supporting_mapping[i] = curr
    return supporting_mapping


def solve_2(input: list) -> int:
    bricks = parse_and_settle(input)

    # brick ID to bricks it supports
    support_mapping = get_supporting_mapping(bricks)
    being_supported_by = get_being_supported_by(support_mapping)

    total = 0
    for i in bricks.keys():
        falling = {i}

        before_size = len(falling)
        after_size = 0

        while before_size != after_size:
            before_size = len(falling)
            for j, v in being_supported_by.items():
                if j != i:
                    if v.intersection(falling) == v:
                        falling.add(j)
            after_size = len(falling)

        total += len(falling) - 1

    return total


if __name__ == "__main__":
    input = read("day22-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 454
    print(solve_2(input))  # 74287
