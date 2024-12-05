from collections import defaultdict

from main.file_reader import read


def solve_1(input: list) -> int:
    left = []
    right = []
    for i in input:
        l, r = i.split()
        left.append(int(l))
        right.append(int(r))

    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))


def solve_2(input: list) -> int:
    left = []
    right = defaultdict(int)
    for i in input:
        l, r = i.split()
        left.append(int(l))
        right[int(r)] = right[int(r)] + 1

    return sum(l * right[l] for l in left)


if __name__ == "__main__":
    input = read("day01-01.txt", "main/year2024/resources")
    print(solve_1(input))  # 2756096
    print(solve_2(input))  # 23117829
