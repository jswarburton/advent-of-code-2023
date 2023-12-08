import math
from functools import reduce

from main.file_reader import read


def solve_1(input: list) -> int:
    instructions, mapping = parse(input)

    steps = 0
    curr = "AAA"

    while True:
        instruction = instructions[steps % len(instructions)]

        left_target, right_target = mapping[curr]
        curr = left_target if instruction == "L" else right_target

        steps += 1

        if curr == "ZZZ":
            return steps


def solve_2(input: list) -> int:
    instructions, mapping = parse(input)

    points = [key for key in mapping.keys() if key.endswith("A")]

    nums = []

    for p in points:
        visited = set()
        steps = 0
        curr = p

        while True:
            instruction = instructions[steps % len(instructions)]

            left_target, right_target = mapping[curr]
            curr = left_target if instruction == "L" else right_target

            steps += 1

            if curr.endswith("Z"):
                if any(
                    v2 % len(instructions) == steps % len(instructions)
                    for v1, v2 in visited
                ):
                    break
                visited.add((curr, steps))

        nums.extend([num for _, num in visited])

    return reduce(math.lcm, nums)


def parse(input):
    instructions = input[0]
    mapping = dict()
    for i in input[2:]:
        source, targets = i.split(" = (")
        targets, _ = targets.split(")")
        t1, t2 = targets.split(", ")

        mapping[source] = (t1, t2)
    return instructions, mapping


if __name__ == "__main__":
    input = read("day08-01.txt")
    print(solve_1(input))  # 16579
    print(solve_2(input))  # 12927600769609
