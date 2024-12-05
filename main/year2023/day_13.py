from main.file_reader import read


def solve_1(input: list) -> int:
    return solve(input)


def solve_2(input: list) -> int:
    return solve(input, diff=1)


def solve(input: list, diff=0) -> int:
    patterns = parse_patterns(input)

    def row_diff(r1, r2):
        return sum(0 if c1 == c2 else 1 for (c1, c2) in zip(r1, r2))

    def reflection_line(pattern):
        for i in range(len(pattern) - 1):
            total_diff = sum(
                row_diff(above, below)
                for above, below in zip(pattern[i::-1], pattern[i + 1 :])
            )
            if total_diff == diff:
                return i + 1
        return 0

    total = 0
    for pattern in patterns:
        total += reflection_line(pattern) * 100 + reflection_line(
            rotate_clockwise(pattern)
        )

    return total


def parse_patterns(input: list):
    patterns = []
    pattern = []
    for i in input:
        if not i:
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(i)
    patterns.append(pattern)
    return patterns


def rotate_clockwise(pattern):
    return ["".join([row[j] for row in pattern]) for j in range(len(pattern[0]))]


if __name__ == "__main__":
    input = read("day13-01.txt", "main/year2023/resources")
    print(solve_1(input))  # 29846
    print(solve_2(input))  # 25401
