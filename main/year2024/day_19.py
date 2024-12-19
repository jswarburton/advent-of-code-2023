from functools import cache

from main.file_reader import read


def solve_1(input: list) -> int:
    patterns, designs = parse(input)

    @cache
    def helper(target):
        if target == "":
            return True

        for s in patterns:
            if target.startswith(s):
                if helper(target[len(s) :]):
                    return True

        return False

    return sum(helper(d) for d in designs)


def solve_2(input: list) -> int:
    patterns, designs = parse(input)

    @cache
    def helper(target):
        if target == "":
            return 1

        count = 0
        for p in patterns:
            if target.startswith(p):
                count += helper(target[len(p):])

        return count

    return sum(helper(d) for d in designs)


def parse(input):
    top_line = input[0]
    patterns = set(top_line.split(", "))
    designs = input[2:]
    return patterns, designs


if __name__ == "__main__":
    input = read("day19-01.txt", "main/year2024/resources")
    print(solve_1(input))  # 336
    print(solve_2(input))  # 758890600222015
