import re

from main.file_reader import read


def solve_1(input: list) -> int:
    total = 0
    for i in input:
        matches = re.findall(r"mul\((\d+),(\d+)\)", i)
        total += sum(int(a) * int(b) for a, b in matches)
    return total


def solve_2(input: list) -> int:
    total = 0
    do = True

    for i in input:
        pattern = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern, i)

        str_matches = [f"mul({match[0]},{match[1]})" for match in matches]

        # requires that there are no duplicate mul(x,y) in the input
        match_indices = [i.find(match) for match in str_matches]

        do_indices = {j for j in range(len(i)) if i.startswith("do()", j)}
        dont_indices = {j for j in range(len(i)) if i.startswith("don't()", j)}

        for j in range(len(i)):
            if j in match_indices and do:
                a, b = matches[match_indices.index(j)]
                total += int(a) * int(b)
            elif j in do_indices:
                do = True
            elif j in dont_indices:
                do = False

    return total


if __name__ == "__main__":
    input = read("day03-01.txt", "main/year2024/resources")
    print(solve_1(input))  # 181345830
    print(solve_2(input))  # 98729041
